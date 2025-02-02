from utils import clean_text, calc_relative_freq, calculate_prob_dist, alphabet, theorical_freq, open_file

def caesar_decrypt(text, shift):
    res =""
    
    # iterate over each character in the text
    for char in text:
        # get the index of the character in the alphabet
        idx =alphabet.index(char)
        # calculate the new index
        new_idx =(idx-shift) % len(alphabet)
        # add the new character to the result
        res += alphabet[new_idx]
            
    return res

def brute_force_caesar(ciphertext, theorical_freq, top_k=5):
    results = []
    
    # clean the text
    clean_ciphertext = clean_text(ciphertext)
    # iterate over each shift
    for shift in range(31):  # 0-30 shifts
        # decrypt the text
        decrypted = caesar_decrypt(clean_ciphertext, shift)
        #calculate the relative frequency of the decrypted text
        observed_freq = calc_relative_freq(decrypted)
        #calculate the distance between the observed and theorical frequencies
        dist = calculate_prob_dist(observed_freq, theorical_freq)
        results.append({
            'shift':shift,
            'dist':dist,
            'decrypted_text':decrypted
        })
    
    #sort the results
    results.sort(key=lambda x: x['dist'])
    #best k results
    return results[:top_k]

if __name__ == "__main__":
    top_k =10
    #open the file
    ciphertext = open_file("cyphers/ceasar.txt")
    
    #execute the brute force
    results =brute_force_caesar(ciphertext,theorical_freq,top_k)
    
    #results
    print(f"\nBest {top_k} candidates:")
    print("-"*50)
    for i, result in enumerate(results, 1):
        print(f"\nCandidate #{i}")
        print(f"Shift: {result['shift']}")
        print(f"Distance: {result['dist']:.4f}")
        print("Decrypted text:")
        print(result['decrypted_text'])
        print("-"*50)