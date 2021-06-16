#!/usr/bin/env python3
""" Die Class File """

__author__ = 'Stephen Lee'
__email__ = 'stephenjonglee@csu.fullerton.edu'
__maintainer__ = 'stephenjonglee'

import random
import time


class Die:
    def __init__(self, n=6):
        self.sides = n

    def roll(self):
        print('Rolling...')
        for i in range(0, 2):
            time.sleep(1)
            print('...')
        return random.randint(1, self.sides)
