# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.before = seed
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1

    def rand(self):
        self.before = (self.a * self.before) % self.m
        return self.before


class ListRand:
    def __init__(self, number_list):

        self.random_number_list = number_list.copy()
        self.current = 0

    def rand(self):
        try:
            random_number = self.random_number_list[self.current]
        except IndexError:
            raise RuntimeError('This index is out of range,'
                               'You have exceeded the length of the list')

        self.current += 1
        return random_number


if __name__ == '__main__':
    rand_class = LCGRand(69)
    rand_list_class = ListRand([45, 32, 12, 54, 31, 22, 11, 85])

    for times in range(5):
        print(f'Random number from LCGRand is {rand_class.rand()},'
              f'Random number from ListRand is {rand_list_class.rand()}')
