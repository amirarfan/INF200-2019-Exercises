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
            self.board = Board.standard_board

        if goal is None:
            self.goal = Board.standard_goal

        self.change_position = 0

    def goal_reached(self, cur_pos):
        return cur_pos >= self.goal

    def position_adjustment(self, positiones):
        if positiones in self.board.keys():
            self.change_position = self.board[positiones]
        else:
            self.change_position = 0

        return self.change_position


class Player:
    def __init__(self, board=None):
        if board is None:
            self.board = Board()
        else:
            self.board = board
        # VI må legge til antall trekk
        self.position = 0

    def move(self):
        self.position += random.randint(1, 6)

        if Board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = Board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        self.position += random.randint(1, 6)
        if self.board.position_adjustment(self.position) == 0:
            pass
        elif self.position > self.board.position_adjustment(self.position):
            self.position = self.board.position_adjustment(
                self.position) + self.extra_steps


class LazyPlayer(Player):
    def __init__(self, board, drop_steps=1):
        super().__init__(board)
        self.drop_steps = drop_steps

    def move(self):
        self.position += random.randint(1, 6)
        if self.board.position_adjustment(self.position) == 0:
            pass
        elif self.position < self.board.position_adjustment(self.position):
            self.position = self.board.position_adjustment(
                self.position) - self.drop_steps

        if self.position < 0:
            self.position = 0

class Simulation:
    def __init__(self, player_classes, board=None, seed=69, randomize_players=False):
        if board is None:
            self.board = Board()
        else:
            self.board = board

        self.player_classes = player_classes

        self.randomtf = randomize_players


    def single_game(self):
        pass
    def run_simulation(self):
        pass
    def get_results(self):
        pass
    def winners_per_type(self):
        pass
    def durations_per_type(self):
        pass
    def players_per_type(self):
        pass



