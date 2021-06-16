#!/usr/bin/env python3
""" Die Class File """

__author__ = 'Stephen Lee'
__email__ = 'stephenjonglee@csu.fullerton.edu'
__maintainer__ = 'stephenjonglee'

import random
import time


class Die:
    """ Class Die with optional sides parameter """
    def __init__(self, n=6):
        self.sides = n

    def roll(self):
        """ Function roll the die and returns a random integer in range """
        print('Rolling...')
        for _ in range(0, 2):
            time.sleep(1)
            print('...')
        return random.randint(1, self.sides)
