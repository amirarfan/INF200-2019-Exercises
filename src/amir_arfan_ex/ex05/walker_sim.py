# -*- coding: utf-8 -*-
import random

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'


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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """

        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        single_walker = Walker(self.start, self.home)

        while not single_walker.is_at_home():
            single_walker.move()

        return single_walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        list_walks = [self.single_walk() for _ in range(num_walks)]

        return list_walks


if __name__ == '__main__':
    sim_0_10_12345 = Simulation(0, 10, 12345)
    sim_10_0_12345 = Simulation(10, 0, 12345)
    sim_0_10_54321 = Simulation(0, 10, 54321)
    sim_10_0_54321 = Simulation(10, 0, 54321)

    for i in range(1, 3):
        print(f'Simulation {i} with seed 12345, from 0 to 10'
              f' {sim_0_10_12345.run_simulation(20)}')
        print(f'Simulation {i} with seed 12345, from 10 to 0'
              f' {sim_10_0_12345.run_simulation(20)}')

    print(f'Simulation 1 with seed 54321 from 0 to 10'
          f'{sim_0_10_54321.run_simulation(20)}')
    print(f'Simulation 1 with seed 54321 from 10 to 0'
          f'{sim_10_0_54321.run_simulation(20)}')
