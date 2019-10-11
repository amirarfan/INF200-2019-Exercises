# -*- coding: utf-8 -*-

__author__ = 'Sebastian Tobias Becker, Amir Inaamullah Arfan'
__email__ = 'sebabeck@nmbu.no, amar@nmbu.no'

import random
import time
from matplotlib import pyplot as plt


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
        87: 70
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
    return {"Player"+str(k):0 for k in range(1,num_players+1)}

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
    winning_state = False
    board = new_board()
    players_and_positions = player_position(num_players)

    while winning_state == False:
        for i in players_and_positions.keys():
            players_and_positions[i] = new_position(players_and_positions[i])
            





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
        List with the numbedr of moves needed in each game.
    """


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
