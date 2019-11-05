# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        """
        __init__ function, that takes only seed as an argument
        """
        self.before = seed
        self.a = 7 ** 5  # Defining a
        self.m = 2 ** 31 - 1  # Defining m
        self.num_i = 0  # Initialising an index

    def rand(self):
        self.before = (self.a * self.before) % self.m  # Generating the random
        # Number
        return self.before

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            self.num_i += 1
            yield self.num_i, self.rand()


class RandIter:
    def __init__(self, rn_generator, length):
        """

            Arguments
            ---------
            rn_generator :
                A random number generator with a ``rand`` method that
                takes no arguments and returns a random number.
            length : int
                The number of random numbers to generate
            """
        self.generator = rn_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
            Initialise the iterator.

            Returns
            -------
            self : RandIter

            Raises
            ------
            RuntimeError
                If iter is called twice on the same RandIter object.
            """
        if self.num_generated_numbers is not None:
            raise RuntimeError('Can only be initialised once for object')
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
            Generate the next random number.

            Returns
            -------
            int
                A random number.

            Raises
            ------
            RuntimeError
                If the ``__next__`` method is called before ``__iter__``.
            StopIteration
                If ``self.length`` random numbers are generated.
            pass
            """
        if self.num_generated_numbers is None:
            raise RuntimeError('Cannot initialize ``__next__`` '
                               'before ``__iter__`` is called')

        print(self.num_generated_numbers)

        if self.num_generated_numbers == self.length:
            raise StopIteration

        random_num = self.generator.rand()
        self.num_generated_numbers += 1
        return random_num


if __name__ == "__main__":

    random_number_generator = LCGRand(1)
    for rand in random_number_generator.random_sequence(10):
        print(rand)

    for i, rand in random_number_generator.infinite_random_sequence():
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
