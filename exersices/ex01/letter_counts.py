def letter_freq(txt):
    """  Function that iterates through a string, adding each letter to the dictionary as well as increasing the
    item value with one if the letter already exists as a key.
    """
    freq = {}  # Initiate an empty dictionary
    for letters in txt.lower():  # Using .lower to have a lowercase string
        if letters not in freq:  # If test to check if letter is already in dict.
            freq[letters] = 1  # Creating a dictionary entry with letter
        else:
            freq[letters] += 1  # If the letter already exists in dictionary, + with one

    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):  # Using sorted python function to get a sorted output
        print('{:3}{:10}'.format(letter, count))
