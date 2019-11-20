# -*- coding: utf-8 -*-

__author__ = "Amir Arfan, Sebastian Tobias Becker"
__email__ = "amar@nmbu.no, sebabeck@nmbu.no"

import chutes_simulation as sa
import pytest


def test_move():
    player = sa.Player()
    first_pos = player.position
    player.move()
    second_pos = player.position
    assert first_pos != second_pos


def test_winner_get_result():
    sim = sa.Simulation([sa.LazyPlayer])
    sim.run_simulation(1)
    assert (sim.get_results()[0][1]) == sa.LazyPlayer.__name__


def test_amount_of_winners_single_game():
    sim = sa.Simulation([sa.LazyPlayer, sa.Player, sa.ResilientPlayer])
    sim.run_simulation(1)
    assert not (len(sim.get_results()) == 2)  # Tests that there is only one
    # winner per game
    assert (len(sim.get_results()) == 1)
