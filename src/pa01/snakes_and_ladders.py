# -*- coding: utf-8 -*-

__author__ = "Sebastian Tobias Becker, Amir Inaamullah Arfan"
__email__ = "sebabeck@nmbu.no, amar@nmbu.no"

import random
import time
import numpy as np


def new_board():
    """
    Returns a board consisting of both snakes and ladder positions
    """
    snakes_and_ladders = {
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
    return snakes_and_ladders


def dice():
    """
    Returns a value between 1 and 6. Simulates a dice throw.
    """
    return random.randint(1, 6)


def new_position(position):
    """
    Returns new position of the player using the dice function.
    """
    position += dice()
    return position


def player_position(num_players):
    return {"Player" + str(k): 0 for k in range(1, num_players + 1)}


def winning_state(position):
    """
    Checks if a player has won
    """
    if position >= 90:
        return True
    else:
        pass


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    completed_game = False
    board = new_board()
    players_and_positions = player_position(num_players)
    num_moves = 0
    start_time = time.time()
    while not completed_game:
        num_moves += 1
        for i in players_and_positions.keys():
            players_and_positions[i] = new_position(players_and_positions[i])
            if players_and_positions[i] in board.keys():
                players_and_positions[i] = board[players_and_positions[i]]
            if winning_state(players_and_positions[i]):
                completed_game = True
    final_time = time.time() - start_time

    return num_moves, final_time


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """

    board = new_board()
    num_moves_list = []
    duration_list = []
    for game in range(num_games):
        players_and_positions = player_position(num_players)
        completed_game = False
        num_moves = 0
        start_time = time.time()
        while not completed_game:
            num_moves += 1
            for i in players_and_positions.keys():
                players_and_positions[i] = new_position(
                    players_and_positions[i]
                )
                if players_and_positions[i] in board.keys():
                    players_and_positions[i] = board[players_and_positions[i]]
                if winning_state(players_and_positions[i]):
                    num_moves_list.append(num_moves)
                    completed_game = True
                    duration_list.append(time.time() - start_time)

    return num_moves_list, duration_list


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    random.seed(seed)
    num_moves_list, duration_list = multiple_games(num_games, num_players)
    return num_moves_list, duration_list


if __name__ == "__main__":
    number_of_moves, durations = multi_game_experiment(100, 4, 2)
    durations.sort()
    first = durations[0]
    last = durations[len(durations) - 1]
    print(
        f"""
    The shortest game duration was {first:2f} 
    The longest game duration was {last:2f}
    The median game duration was {np.median(durations):2f}
    The mean game duration was {np.mean(durations):2f} 
    The standard deviation was {np.std(durations):2f}
    """
    )
