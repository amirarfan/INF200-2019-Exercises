# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan, Sebastian Tobias Becker'
__email__ = 'amar@nmbu.no, sebabeck@nmbu.no'


class Board:
    standard_board = {
        1: 40,
        8: 10,
        36: 52,
        43: 62,
        49: 79,
        65: 82,
        68: 85,
        24: 5,
        33: 3,
        42: 30,
        56: 37,
        64: 27,
        74: 12,
        87: 70,
    }

    standard_goal = 90

    def __init__(self, ladders_and_snakes=None, goal=None):

        if ladders_and_snakes is None:
            self.board = self.standard_board

        if goal is None:
            self.goal = self.standard_goal

        self.position = 0

    def goal_reached(self):
        return if self.position >= self.goal

    def position_adjustment(self):
        pass
