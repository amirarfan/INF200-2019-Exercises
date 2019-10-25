# -*- coding: utf-8 -*-

__author__ = 'Amir Arfan'
__email__ = 'amar@nmbu.no'

import random


class Walker:
    def __init__(self, start_position, home_position):
        self.current_position = start_position
        self.final_position = home_position
        self.current_steps = 0

    def move(self):
        self.current_position += random.choice([-1, 1])
        self.current_steps += 1

    def is_at_home(self):
        return self.current_position == self.final_position

    def get_position(self):
        return self.current_position

    def get_steps(self):
        return self.current_steps


def walker_start_home(start_position, home_position):
    walker = Walker(start_position, home_position)

    while not walker.is_at_home():
        walker.move()

    return walker.get_steps()
