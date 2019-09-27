def char_counts(textfilename):
    """
    Counts how many time each character code (1-256) occurs.

    Returns a list with each index being the ord value of the character and
    index value being how many times it occurred

    """
    result = [0 for _ in range(255+1)]
    # Result contains only 0's for computational purposes
    with open(textfilename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
        for char in set(data):
            # Using sets:
            # so that it only has to check for the ord´s that is in the string
            index = ord(char)
            # Could have done this without using sets:
            # But it would be less effective
            result[index] = data.count(char)
        return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
