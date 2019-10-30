# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'

import random


class Walker:
    def __init__(self, start_position, home_position):
        """

        Init function that takes in two arguments that are to be used
        throughout the class.

        """
        self.current_position = start_position
        self.final_position = home_position
        self.current_steps = 0

    def move(self):
        """
        Simulates a move, using python's integrated random function

        """
        self.current_position += random.choice([-1, 1])
        self.current_steps += 1

    def is_at_home(self):
        """
        Checks if the walker is at home by using a bool test

        """
        return self.current_position == self.final_position

    def get_position(self):
        """
        Simple function that returns the current position

        """
        return self.current_position

    def get_steps(self):
        """
        Simple function that returns the current amount of steps taken.
        """
        return self.current_steps


def walker_start_home(start_position, home_position):
    """
    Walker function that simulates a walk through using
    the 'Walker class'

    """
    walker = Walker(start_position, home_position)

    while not walker.is_at_home():
        walker.move()

    return walker.get_steps()


if __name__ == "__main__":
    random.seed(100) # Allocating a seed for test purposes
    num_sim = 5
    dist = [2, 5, 10, 20, 50, 100]
    for distance in dist:
        result_list = [walker_start_home(0, distance) for simulations
                       in range(num_sim)]
        print(f'Distance: {distance} --> Path: {result_list}')
