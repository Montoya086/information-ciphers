from utils import clean_text, calc_relative_freq, calculate_prob_dist, alphabet, theorical_freq, open_file

vigenere_table = dict()
#fill the vigenere table
for i in range(len(alphabet)):
    # create a new dictionary for each letter in the alphabet
    vigenere_table[alphabet[i]] = dict()
    # fill the dictionary with the vigenere cipher
    for j in range(len(alphabet)):
        vigenere_table[alphabet[i]][alphabet[j]] = alphabet[(i+j) % len(alphabet)]

def decypher(text, key):
    # convert text to lowercase
    text = text.lower()
    # result string
    result = ""
    # iterate over each letter in the text
    for i in range(len(text)):
        # add the padded letter to the result
        for letter in vigenere_table[key[i%len(key)]]:
            if vigenere_table[key[i%len(key)]][letter] == text[i]:
                result += letter
    return result

def generate_keys():
    keys = []
    key_prefix = "pa"  #known prefix
    
    #generate keys of length 2 to 6 (as we know the prefix is 2 characters long)
    for length in range(2, 7):
        if length == 2:
            #for length 2, we only need to add the prefix
            keys.append(key_prefix)
        else:
            #generate all possible keys of length 2 to 6 that start with 'pa'
            def generate_combinations(current_key,remaining_length):
                """
                    source: ClaudeIA
                    propmt: How to generate all possible combinations of a string in Python given a length
                """
                if len(current_key) == length:
                    keys.append(current_key)
                    return
                
                for letter in alphabet:
                    generate_combinations(current_key+letter, remaining_length-1)
            
            generate_combinations(key_prefix, length - 2)
    
    return keys

def brute_force_vigenere(ciphertext, top_k=5):
    results = []
    
    #clean the text
    clean_ciphertext =clean_text(ciphertext)
    
    #generate possible keys
    possible_keys =generate_keys()
    
    #iterate over each key
    for key in possible_keys:
        # print one key every 1000
        if possible_keys.index(key)%1000 == 0:
            print(f"Trying with key: {key} ({possible_keys.index(key)})")
        try:
            #decrypt the text
            decrypted = decypher(clean_ciphertext, key)
            #calculate the relative frequency of the decrypted text
            observed_freq = calc_relative_freq(decrypted)
            
            # calculate the distance between the observed and theorical frequencies
            dist = calculate_prob_dist(theorical_freq, observed_freq)
            results.append({
                'key': key,
                'dist': dist,
                'decrypted_text': decrypted
            })
            
        except Exception as _:
            continue
    
    #sort the results
    results.sort(key=lambda x: x['dist'])
    
    #best k results
    return results[:top_k]

def main():
    best_k = 10
    #open the file
    ciphertext = open_file("cyphers/vigenere.txt")
    
    #execute the brute force
    results = brute_force_vigenere(ciphertext, best_k)
    
    #results
    print(f"\nBest {best_k} candidates:")
    print("-"*50)
    for i, result in enumerate(results, 1):
        print(f"\nCandidate #{i}")
        print(f"Key: {result['key']}")
        print(f"Key Lenght: {len(result['key'])}")
        print(f"Distance: {result['dist']:.4f}")
        print(f"Decrypted text:")
        print(result['decrypted_text'])
        print("-"*50)

if __name__ == "__main__":
    main()