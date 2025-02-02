import sys
# get the absolute path of this file
absolutepath = sys.path[0]
sys.path.append(absolutepath + "/../P1")
from clean import clean_text
alphabet = "abcdefghijklmnñopqrstuvwxyz"

def calc_freq(text, alphabet):
    # convert text to lowercase
    text = text.lower()
    # result dictionary
    freq = dict()
    #fill the dictionary with the alphabet on 0
    for letter in alphabet:
        freq[letter] = 0
    # iterate over each letter in the text
    for letter in text:
        # add the letter to the result
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq

def calc_prob(freq, total):
    # result dictionary
    prob = dict()
    # iterate over each letter in the frequency dictionary
    for letter in freq:
        # calculate the probability of the letter
        prob[letter] = freq[letter] / total
    return prob

def generate_table(text, alphabet):
    freq = calc_freq(text, alphabet)
    total = sum(freq.values())
    prob = calc_prob(freq, total)
    return freq, prob

if __name__ == "__main__":
    text = input("Enter text: ")
    text = clean_text(text, alphabet)

    freq, prob = generate_table(text, alphabet)
    print("Frequency table:")
    print(freq)
    print("Probability table:")
    print(prob)