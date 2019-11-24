# -*- coding: utf-8 -*-

__author__ = "Amir Arfan, Sebastian Tobias Becker"
__email__ = "amar@nmbu.no, sebabeck@nmbu.no"

import random


class Board:
    """
    Board Class, creates a board
    """
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

    def __init__(self, snakes_and_ladders=None, goal=None):
        """

        :param snakes_and_ladders: Dictionary board
        :param goal: Int value if goal is reached player wins.
        """

        if snakes_and_ladders is None:
            self.board = Board.standard_board

        if goal is None:
            self.goal = Board.standard_goal

        self.change_position = 0

    def goal_reached(self, cur_pos):
        """

        :param cur_pos: Takes current position as input, integer value.
        :return: Returns True or False whether player has reached goal
        """
        return cur_pos >= self.goal

    def position_adjustment(self, cur_pos):
        """

        :param cur_pos: Takes in the current position as input, integer
        :return: Returns the new position after checking the dictionary(board)
        """
        if cur_pos in self.board.keys():
            self.change_position = self.board[cur_pos]
        else:
            self.change_position = 0

        return self.change_position


class Player:
    """
    Player Class
    """
    def __init__(self, board):
        """
        :param board: takes in board as input, determines which board the
        player shall play on
        """
        self.board = board
        self.num_moves = 0
        self.position = 0

    def move(self):
        """
        Moves the player , by throwing a dice done with random function.
        Updates the position and increases the number of moves.

        """
        self.position += random.randint(1, 6)

        if self.board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = self.board.position_adjustment(self.position)
        self.num_moves += 1


class ResilientPlayer(Player):
    """
    Resilient Player class, this player takes one extra step the next round
    if he fell down in the previous round.
    """
    def __init__(self, board, extra_steps=1):
        """

        :param board: Takes in board as input
        :param extra_steps: Takes in amount of steps he should take as input
        """
        super().__init__(board)
        self.extra_steps = extra_steps
        self.went_down = False

    def move(self):
        """
        Moves the ResilientPlayer, done with if tests.
        Updates the current position and increases the number of moves taken.
        Simple bool if test to check whether the player should take an extra
        step.

        """
        if self.went_down:
            self.position += random.randint(1, 6) + self.extra_steps
        else:
            self.position += random.randint(1, 6)

        if self.position > self.board.position_adjustment(self.position):
            self.went_down = True
        else:
            self.went_down = False

        if self.board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = self.board.position_adjustment(self.position)

        self.num_moves += 1


class LazyPlayer(Player):
    """
    LazyPlayer class, this player takes one step backwards next round
     if he climbed in the previous round.
    """
    def __init__(self, board, dropped_steps=1):
        """

        :param board: Takes board as input
        :param dropped_steps:  Takes amount fo steps he should drop next round
        """
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.went_up = False

    def move(self):
        """
        Move function, moves player. Basically the same as ResilientPlayer,
        however this one does a simple bool test to check wheter the player
        should drop steps.

        """
        if self.went_up:
            self.position += random.randint(1, 6) + self.drop_steps
        else:
            self.position += random.randint(1, 6)

        if self.position < self.board.position_adjustment(self.position):
            self.went_up = True
        else:
            self.went_up = False

        if self.board.position_adjustment(self.position) == 0:
            pass
        else:
            self.position = self.board.position_adjustment(self.position)

        self.num_moves += 1


class Simulation:
    """
    Simulation class to simulate games using the different Player classes.
    """
    def __init__(
        self, player_field, board=None, seed=69, randomize_players=False
    ):
        """

        :param player_field: This is a list containing classes of the different
        players.
        :param board: The board the players should play on
        :param seed: Seed for the random module
        :param randomize_players: Whether or not the order of players should be
        shuffleed.
        """
        if board is None:
            self.board = Board()
        else:
            self.board = board

        self.player_classes = player_field

        self.randomtf = randomize_players

        random.seed(seed)
        self.res_simulation = []

        self.types_of_players = [
            type_player.__name__ for type_player in player_field
        ]

    def single_game(self):
        """
        Simulates a single game

        """

        if self.randomtf:
            random.shuffle(self.player_classes)

        players = [player(self.board) for player in self.player_classes]
        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.num_moves, type(player).__name__

    def run_simulation(self, number_of_simulation):
        """
        Simulates the amount of games which is given as input.

        """
        for simulation in range(number_of_simulation):
            self.res_simulation.append(self.single_game())

    def get_results(self):
        """

        :return: Returns the result list containing winners.
        """
        return self.res_simulation

    def winners_per_type(self):
        """

        :return: Returns the winners per type, using zip and dict comprehension
        """
        winners = list(zip(*self.res_simulation))

        winner_dict = {
            player: winners[1].count(player)
            for player in self.types_of_players
        }

        return winner_dict

    def durations_per_type(self):
        """

        :return: Returns the duration per player type, using dict comprehension
        and a list comprehension combined with a for loop.
        """
        duration_dict = {
            type_player: 0 for type_player in self.types_of_players
        }
        for type_player in duration_dict.keys():
            duration_dict[type_player] = [
                duration
                for duration, player in self.res_simulation
                if type_player == player
            ]

        return duration_dict

    def players_per_type(self):
        """

        :return: Returns player  per type. Counting through the player classes
        """
        players_dict = {players.__name__: 0 for players in self.player_classes}
        for players in self.player_classes:
            players_dict[players.__name__] += 1
        return players_dict


if __name__ == "__main__":
    player_classes = [LazyPlayer, Player, ResilientPlayer]
    sim = Simulation(player_classes)
    sim.run_simulation(10)
    print(sim.get_results())
    print(sim.winners_per_type())
    print(sim.durations_per_type())
    print(sim.players_per_type())
