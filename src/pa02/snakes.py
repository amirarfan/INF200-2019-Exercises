# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan, Sebastian Tobias Becker'
__email__ = 'amar@nmbu.no, sebabeck@nmbu.no'

import random


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
        self.change_position = 0

    def goal_reached(self):
        return self.position >= self.goal

    def position_adjustment(self, positiones):
        if positiones in self.board.keys():
            self.change_position = self.board[positiones]
        else:
            self.change_position = 0

        return self.change_position


class Player(Board):
    def __init__(self, board=None):
        if board is None:
            self.board = Board()
        else:
            self.board = board

        super().__init__(self.position)

    def move(self):
        self.position += random.randint(1,6)

        if Board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = Board.position_adjustment(self.position)




