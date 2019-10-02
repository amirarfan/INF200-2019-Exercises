def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squares = []  # Initiate an empty list
    for k in range(n):  # Create a for loop which iterates in range n
        if k % 3 == 1:  # Modulus if test
            squares.append(
                (k ** 2)
            )  # If the if test is correct the 'k' is added to squares
            # If the if test requirement is not fulfilled nothing happens
    return squares


if __name__ == "__main__":
    if squares_by_comp(10) != squares_by_loop(10):
        print("ERROR!")
