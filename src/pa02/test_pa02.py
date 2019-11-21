# -*- coding: utf-8 -*-

__author__ = "Amir Arfan, Sebastian Tobias Becker"
__email__ = "amar@nmbu.no, sebabeck@nmbu.no"

import chutes_simulation as sa
import pytest  # Pep8 tells me to remove this, but crucial for the testing


def test_move():
    """
    Tests whether the player has moved a position
    """
    player = sa.Player(sa.Board())
    first_pos = player.position
    player.move()
    second_pos = player.position
    assert first_pos != second_pos


def test_winner_get_result():
    """
    Tests that the winner is correct
    """
    sim = sa.Simulation([sa.LazyPlayer])
    sim.run_simulation(1)
    assert (sim.get_results()[0][1]) == sa.LazyPlayer.__name__


def test_amount_of_winners_single_game():
    """
    Test that there is only one winner per game
    """
    sim = sa.Simulation([sa.LazyPlayer, sa.Player, sa.ResilientPlayer])
    sim.run_simulation(1)
    assert not (len(sim.get_results()) == 2)  # Assert not to check that the
    # value is not higher than one.
    assert len(sim.get_results()) == 1


def test_steps_taken():
    """
    Test to assure that no one can win without taking any steps

    """
    sim = sa.Simulation([sa.LazyPlayer, sa.Player, sa.ResilientPlayer])
    sim.run_simulation(1)
    assert sim.get_results()[0][0] > 0


def test_shuffle():
    """
     Tests if player list actually gets shuffled if told so
    """
    player_list = [sa.LazyPlayer, sa.Player, sa.ResilientPlayer]
    sim = sa.Simulation(
        [sa.LazyPlayer, sa.Player, sa.ResilientPlayer], randomize_players=True
    )
    sim.single_game()
    assert player_list != sim.player_classes


def test_player_per_type():
    """
    Tests if amount of player per type gives correct output
     """
    player_list = [sa.LazyPlayer, sa.LazyPlayer, sa.Player, sa.ResilientPlayer]
    sim = sa.Simulation(player_list)
    sim.run_simulation(1)
    assert sim.players_per_type()["LazyPlayer"] == 2
    assert sim.players_per_type()["Player"] == 1
    assert not sim.players_per_type()["ResilientPlayer"] == 2


def test_resilient_player_wins():
    """
    From how Resilient player is coded, he should win given a higher amount
    of simulations and the same seed
    """

    player_list = [sa.LazyPlayer, sa.Player, sa.ResilientPlayer]
    sim = sa.Simulation(player_list)
    sim.run_simulation(1)
    winner_types = sim.winners_per_type()
    assert (
        winner_types["ResilientPlayer"] > winner_types["LazyPlayer"]
        and winner_types["ResilientPlayer"] > winner_types["Player"]
    )
