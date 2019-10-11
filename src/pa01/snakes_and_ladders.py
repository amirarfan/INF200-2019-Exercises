# -*- coding: utf-8 -*-

__author__ = 'Sebastian Tobias Becker, Amir Inaamullah Arfan'
__email__ = 'sebabeck@nmbu.no, amar@nmbu.no'

import random
import time
from matplotlib import pyplot as plt

def board():
    snakes_and_laders={
        1:40,
        8:10,
        36:52,
        43:62,
        49:79,
        65:82,
        68:85,
        24:5,
        33:3,
        42:30,
        56:37,
        64:27,
        74:12,
        87:70
    }
    return snakes_and_laders

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
        List with the numbedr of moves needed in each game.
    """