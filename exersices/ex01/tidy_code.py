from random import randint


__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'


def randomnumgen():
    """
    A function which generates a random number with the sum of two numbers between 1 and 6
    """
    return randint(1, 6) + randint(1, 6)  # Used randint for clarity, as randint refers to random integer.


def guessanumber():  # Guess a number function
    """ Guess a number function. As long as the guessed number is below 1, the function will continue to sk for a number
    """
    num_guess = 0
    while num_guess < 1:
        num_guess = int(input('Guess a number greater than one. Your guess: '))
    return num_guess


def checkguessrandom(rand_num, guess_num):
    """
    Checks if the random number is equal to the guessed number. Returns a True or False value (BOOL)
    """
    return rand_num == guess_num


if __name__ == '__main__':

    bool_test = False  # Variable is set as false from the beginning, to be changed to True if user is able to guess
    #  the random number
    points = 3  # The user begins with 3 points
    num_to_guess = randomnumgen()
    while not bool_test and points > 0:  # While loop which runs until user is able to guess the random number or has
        # lost all points
        your_guess = guessanumber()
        check = checkguessrandom(num_to_guess, your_guess)
        if check:
            bool_test = True
        else:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print(f'You won {points} points.')
    else:
        print(f'You lost. Correct answer: {num_to_guess}.')
