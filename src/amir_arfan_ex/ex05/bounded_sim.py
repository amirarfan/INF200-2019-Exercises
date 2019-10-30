# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'

from walker_sim import Walker, Simulation


class BoundedWalker:
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

        if not left_limit <= start <= right_limit:
            print('Your limits are not correct.')
            return
        if not left_limit <= home <= right_limit:
            raise RuntimeError('Your limits are not correct')
            return

        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start,home)  # Using the super method as advised to do
