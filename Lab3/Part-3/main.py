import os
import time
import psutil
import matplotlib.pyplot as plt
from Crypto.Cipher import ChaCha20, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from multiprocessing import Process, Queue

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # convert to MB

def test_chacha20(data, repetitions=1000):
    memory_before = get_memory_usage()
    start_time = time.time()
    
    for _ in range(repetitions):
        # Generate key and nonce
        key = get_random_bytes(32)  # 256 bits
        nonce = get_random_bytes(12)
        
        # Encrypt
        cipher = ChaCha20.new(key=key, nonce=nonce)
        ciphertext = cipher.encrypt(data)
        
        # Decrypt
        cipher = ChaCha20.new(key=key, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        
        assert plaintext == data
    
    total_time = time.time() - start_time
    memory_after = get_memory_usage()
    
    return {
        "total_time": total_time,
        "average_time": total_time / repetitions,
        "memory_before": memory_before,
        "memory_after": memory_after,
        "memory_used": memory_after - memory_before
    }

def test_aes_cbc(data, repetitions=1000):
    memory_before = get_memory_usage()
    start_time = time.time()
    
    for _ in range(repetitions):
        # Generate key and IV
        key = get_random_bytes(32)  # AES-256
        iv = get_random_bytes(16)
        
        # Encrypt (with padding)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        
        # Decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        # Basic verification
        assert plaintext == data
    
    total_time = time.time() - start_time
    memory_after = get_memory_usage()
    
    return {
        "total_time": total_time,
        "average_time": total_time / repetitions,
        "memory_before": memory_before,
        "memory_after": memory_after,
        "memory_used": memory_after - memory_before
    }

def test_aes_ecb(data, repetitions=1000):
    memory_before = get_memory_usage()
    start_time = time.time()
    
    for _ in range(repetitions):
        # Generate key
        key = get_random_bytes(32)  # AES-256
        
        # Encrypt (with padding)
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        
        # Decrypt
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        assert plaintext == data
    
    total_time = time.time() - start_time
    memory_after = get_memory_usage()
    
    return {
        "total_time": total_time,
        "average_time": total_time / repetitions,
        "memory_before": memory_before,
        "memory_after": memory_after,
        "memory_used": memory_after - memory_before
    }

def run_algorithm_in_process(algorithm_func, data, repetitions, queue):
    """
    DEV NOTE:
    This function is used to run the algorithm in a separate process.
    It is used to avoid the garbage collector affecting the results.
    """
    result = algorithm_func(data, repetitions)
    queue.put(result)

def compare_ciphers(data_sizes=[1024, 10240, 102400, 1024000]):
    results = []
    
    for data_size in data_sizes:
        print(f"\nTest with {data_size} bytes:")
        # Generate data
        data = get_random_bytes(data_size)
        
        # Adjust repetitions based on the size
        repetitions = max(100, 10000 // data_size)
        
        # Queues to collect results
        chacha_queue = Queue()
        aes_cbc_queue = Queue()
        aes_ecb_queue = Queue()
        
        # Create processes
        chacha_process = Process(target=run_algorithm_in_process, 
                               args=(test_chacha20, data, repetitions, chacha_queue))
        aes_cbc_process = Process(target=run_algorithm_in_process, 
                                args=(test_aes_cbc, data, repetitions, aes_cbc_queue))
        aes_ecb_process = Process(target=run_algorithm_in_process, 
                                args=(test_aes_ecb, data, repetitions, aes_ecb_queue))
        
        # Start processes
        chacha_process.start()
        aes_cbc_process.start()
        aes_ecb_process.start()
        
        # Wait for processes to finish and get results
        chacha_result = chacha_queue.get()
        aes_cbc_result = aes_cbc_queue.get()
        aes_ecb_result = aes_ecb_queue.get()
        
        # Join processes
        chacha_process.join()
        aes_cbc_process.join()
        aes_ecb_process.join()
        
        # Print results
        print(f"ChaCha20: {chacha_result['average_time']*1000:.4f} ms/op, {chacha_result['memory_used']:.4f} MB")
        print(f"AES-CBC:  {aes_cbc_result['average_time']*1000:.4f} ms/op, {aes_cbc_result['memory_used']:.4f} MB")
        print(f"AES-ECB:  {aes_ecb_result['average_time']*1000:.4f} ms/op, {aes_ecb_result['memory_used']:.4f} MB")
        
        results.append({
            "data_size": data_size,
            "chacha20": chacha_result,
            "aes_cbc": aes_cbc_result,
            "aes_ecb": aes_ecb_result
        })
    
    return results

def generate_graphs(results):
    data_sizes = [r["data_size"] for r in results]
    chacha_times = [r["chacha20"]["average_time"]*1000 for r in results]  # ms
    aes_cbc_times = [r["aes_cbc"]["average_time"]*1000 for r in results]  # ms
    aes_ecb_times = [r["aes_ecb"]["average_time"]*1000 for r in results]  # ms
    
    chacha_memory = [r["chacha20"]["memory_used"] for r in results]
    aes_cbc_memory = [r["aes_cbc"]["memory_used"] for r in results]
    aes_ecb_memory = [r["aes_ecb"]["memory_used"] for r in results]
    
    # Create figure with two subplots
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Time graph
    ax1.plot(data_sizes, chacha_times, 'o-', label='ChaCha20')
    ax1.plot(data_sizes, aes_cbc_times, 's-', label='AES-CBC')
    ax1.plot(data_sizes, aes_ecb_times, '^-', label='AES-ECB')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Data size (bytes)')
    ax1.set_ylabel('Average time (ms)')
    ax1.set_title('Comparison of times')
    ax1.legend()
    ax1.grid(True)
    
    # Memory graph
    ax2.plot(data_sizes, chacha_memory, 'o-', label='ChaCha20')
    ax2.plot(data_sizes, aes_cbc_memory, 's-', label='AES-CBC')
    ax2.plot(data_sizes, aes_ecb_memory, '^-', label='AES-ECB')
    ax2.set_xscale('log')
    ax2.set_xlabel('Data size (bytes)')
    ax2.set_ylabel('Memory usage (MB)')
    ax2.set_title('Comparison of memory usage')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('results.png')
    plt.show()

if __name__ == "__main__":
    sizes = [1024, 10240, 102400, 1024000, 10240000]
    results = compare_ciphers(sizes)
    
    # Generate graphs
    generate_graphs(results)