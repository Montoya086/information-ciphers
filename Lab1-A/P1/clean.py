def clean_text(text, alphabet):
    # convert text to lowercase
    text = text.lower()
    # result string
    res = ""
    # iterate over each letter in the text
    for letter in text:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the letter to the result
            res += letter
    return res