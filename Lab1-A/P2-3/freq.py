import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import tabulate
# get the absolute path of this file
absolutepath = sys.path[0]
sys.path.append(absolutepath + "/../P1")
from clean import clean_text

# theorical frequency of the spanish language
theorical_freq = {
    "a": 0.1253,
    "b": 0.0142,
    "c": 0.0468,
    "d": 0.0586,
    "e": 0.1368,
    "f": 0.0069,
    "g": 0.0101,
    "h": 0.0070,
    "i": 0.0625,
    "j": 0.0044,
    "k": 0.0002,
    "l": 0.0497,
    "m": 0.0315,
    "n": 0.0671,
    "ñ": 0.0031,
    "o": 0.0868,
    "p": 0.0251,
    "q": 0.0088,
    "r": 0.0687,
    "s": 0.0798,
    "t": 0.0463,
    "u": 0.0291,
    "v": 0.0111,
    "w": 0.0008,
    "x": 0.0022,
    "y": 0.0088,
    "z": 0.0047
}

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

def calculate_diff_table(freq):
    diff = dict()
    for letter in freq:
        diff[letter] = abs(theorical_freq[letter] - freq[letter])
    return diff

def plot_freq(freq, title):
    # compare the theorical frequency with the frequency of the text
    df = pd.DataFrame({
        "Letter": list(freq.keys()),
        "Real": list(freq.values()),
        "Theoretical": [theorical_freq[letter] for letter in freq.keys()]
    })
    # restructure the data for side-by-side bars
    df_melted = pd.melt(df, 
                       id_vars=['Letter'], 
                       value_vars=['Real', 'Theoretical'],
                       var_name='Type',
                       value_name='Frequency')
    
    # create the plot
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, 
                x="Letter", 
                y="Frequency", 
                hue="Type",
                palette=["skyblue", "red"])
    
    plt.title(title)
    plt.legend()
    plt.show()  

if __name__ == "__main__":
    text = input("Enter text: ")
    text = clean_text(text, alphabet)

    should_plot = False

    if len(sys.argv) == 2:
        if sys.argv[1] == "-p":
            should_plot = True
        else:
            print("Invalid argument")
            sys.exit(1)

    freq, prob = generate_table(text, alphabet)
    print("\nFrequency table:")
    print(tabulate.tabulate(freq.items(), headers=["Letter", "Frequency"]))
    print("\nProbability table:")
    print(tabulate.tabulate(prob.items(), headers=["Letter", "Probability"]))
    print("\nDifference table:")
    diff = calculate_diff_table(prob)
    print(tabulate.tabulate(diff.items(), headers=["Letter", "Difference"]))

    if should_plot:
        plot_freq(prob, "Theorical vs Text frequency of the spanish language")