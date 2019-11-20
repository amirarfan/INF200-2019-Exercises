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
        self.num_moves = 0
        self.position = 0

    def move(self):
        self.position += random.randint(1, 6)

        if self.board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = self.board.position_adjustment(self.position)
        self.num_moves += 1


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
        self.num_moves += 1


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
        self.num_moves += 1


class Simulation:
    def __init__(self, player_classes, board=None, seed=69,
                 randomize_players=False):
        if board is None:
            self.board = Board()
        else:
            self.board = board

        self.player_classes = player_classes

        self.randomtf = randomize_players

        random.seed(seed)
        self.res_simulation = []

        self.types_of_players = [type_player for type_player
                                 in player_classes]

    def single_game(self):

        if self.randomtf:
            random.shuffle(self.player_classes)

        players = [eval(player)(self.board) for player in self.player_classes]
        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.num_moves, type(player).__name__

    def run_simulation(self, number_of_simulation):
        for simulation in range(number_of_simulation):
            self.res_simulation.append(self.single_game())

    def get_results(self):
        return self.res_simulation

    def winners_per_type(self):
        winners = list(zip(*self.res_simulation))
        print(winners)

        winner_dict = {player: winners[1].count(player) for player
                       in self.types_of_players}

        return winner_dict

    def durations_per_type(self):
        duration_dict = {type_player: 0 for type_player in
                         self.types_of_players}
        for type_player in duration_dict.keys():
            duration_dict[type_player] = [duration for duration, player in
                                          self.res_simulation
                                          if type_player == player]

        return duration_dict

    def players_per_type(self):
        pass


if __name__ == "__main__":
    player_classes = ['LazyPlayer', 'Player', 'ResilientPlayer']
    sim = Simulation(player_classes)
    sim.run_simulation(10)
    print(sim.winners_per_type())
    print(sim.durations_per_type())
