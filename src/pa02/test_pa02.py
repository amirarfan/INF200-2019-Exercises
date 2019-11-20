import snakes as sa
import pytest

def test_move():
    player=sa.Player()
    first_pos=player.position
    player.move()
    second_pos = player.position
    assert first_pos != second_pos