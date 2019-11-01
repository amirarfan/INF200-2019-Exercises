# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'

from walker_sim import *


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        if not (left_limit <= start <= right_limit):
            raise RuntimeError('Your limits are not correct')
        elif not (left_limit <= home <= right_limit):
            raise RuntimeError('Your limits are not correct')

        super().__init__(start, home)

        # Using the subclass method as advised to do

        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        """
        Moves the walker with if tests such that the walker cannot move past
        limit

        """
        super().move()  # I am using the move function from the "Walker" Class
        if self.current_position < self.left_limit:
            self.current_position = self.left_limit
        elif self.current_position > self.right_limit:
            self.current_position = self.right_limit

        #  Enforcing the limits


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        if not (left_limit <= start <= right_limit):
            raise RuntimeError('Your limits are not correct')
        elif not (left_limit <= home <= right_limit):
            raise RuntimeError('Your limits are not correct')

        # Added the same if test here as well, such that when you create the
        # simulation class you will already know if your limits are wrong

        super().__init__(start, home, seed)  # Using subclass method
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_bounded_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        single_bounded_walker = BoundedWalker(self.start, self.home,
                                              self.left_limit,
                                              self.right_limit)

        while not single_bounded_walker.is_at_home():
            single_bounded_walker.move()

        return single_bounded_walker.get_steps()

    def run_bounded_simulation(self, num_walks):
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

        list_walks = []
        for _ in range(num_walks):
            list_walks.append(self.single_bounded_walk())

        return list_walks


if __name__ == '__main__':
    boundaries = [0, -10, -100, -1000, -10000]
    rb = 20
    start_pos = 0
    end_pos = 20
    for lb in boundaries:
        current_sim = BoundedSimulation(start_pos, end_pos, 69, lb, rb)
        steps = current_sim.run_bounded_simulation(20)
        print(f'With left-boundary {lb}, steps: {steps}')
