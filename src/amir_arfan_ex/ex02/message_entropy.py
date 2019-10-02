from collections import Counter
from math import log2


def letter_freq(txt):
    return Counter(txt.lower())


def entropy(message):

    """
    Calculates the entropy in a message, and returns the value of the entropy.

    """
    message = message.lower()
    message = message.replace(" ", "")
    # Remove spaces so that they are not counted
    h_ent = 0  # Initiate an entropy value
    n_length = len(message)  # Calculate the length of the message
    n_freq = letter_freq(message)  # Use the letter_freq function
    for i in set(message):
        p_i = n_freq[i] / n_length
        try:  # Using a try test in case log2 = 0, which gives ValueError
            h_ent += p_i * log2(p_i)
        except ValueError:
            break
    return abs(h_ent)


if __name__ == "__main__":
    for msg in "", "aaaa", "aaba", "abcd", "This is a short text.":
        print("{:25}: {:8.3f} bits".format(msg, entropy(msg)))
