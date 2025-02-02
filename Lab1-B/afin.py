from utils import alphabet, theorical_freq, clean_text, calc_relative_freq, open_file, calculate_prob_dist

# greatest common divisor
def mcd(a, m):
    """
    Source: ClaudeIA
    Promt: how to calculate the greatest common divisor of two numbers in Python
    """
    while m:
        a, m = m, a % m
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        # if the product of a and x modulo m is equal to 1, return x
        if ((a % m)*(x % m)) % m ==1:
            return x
    return None

def decypher_afines(text, a, b):
    # convert text to lowercase
    text = text.lower()
    # result string
    res = ""
    a_inv = mod_inverse(a, len(alphabet))
    # iterate over each letter in the text
    for letter in text:
        # add the padded letter to the result
        res += alphabet[(a_inv *(alphabet.index(letter) -b)) % len(alphabet)]
    return res

def brute_force(ciphertext, top_k=5):
    results = []
    m =len(alphabet)
    
    #clean the text
    clean_ciphertext = clean_text(ciphertext)
    
    #iterate over each a and b
    for a in range(1, 17):  # 1 to 16
        #validate the key
        if mcd(a, m) != 1:
            continue
            
        #calculate the modular inverse
        if mod_inverse(a, m) is None:
            continue
            
        for b in range(1, 17): # 1 to 16 for b
            try:
                #descypher the text
                decrypted = decypher_afines(clean_ciphertext, a, b)
                
                #calculate the relative frequency of the decrypted text
                observed_freq = calc_relative_freq(decrypted)
                
                #calculate the distance between the observed and theorical frequencies
                dist = calculate_prob_dist(theorical_freq, observed_freq)
                
                results.append({
                    'a': a,
                    'b': b,
                    'dist': dist,
                    'decrypted_text': decrypted
                })
                
            except Exception as _:
                continue
    
    # sort the results
    results.sort(key=lambda x: x['dist'])
    
    # best k results
    return results[:top_k]

def main():
    top_k = 10
    ciphertext = open_file("cyphers/afines.txt")
    
    # execute the brute force
    results = brute_force(ciphertext, top_k)
    
    #results
    print(f"\nBest {top_k} candidates:")
    print("-"*50)
    for i, result in enumerate(results, 1):
        print(f"\nCandidate #{i}")
        print(f"a = {result['a']}, b = {result['b']}")
        print(f"Distance: {result['dist']:.4f}")
        print("Decrypted text:")
        print(result['decrypted_text'])
        print("-"*50)

if __name__ == "__main__":
    main()