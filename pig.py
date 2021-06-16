#!/usr/bin/env python3
""" Pig Class File """

__author__ = 'Stephen Lee'
__email__ = 'stephenjonglee@csu.fullerton.edu'
__maintainer__ = 'stephenjonglee'

import time
from player import Player
from die import Die


class Pig:
    """ Class Pig game with number of players, list of players, and a die """
    def __init__(self, num=0):
        self.num_players = num
        self.player_list = []
        self.end = False
        self.die = Die()

    def get_num_players(self):
        """ Function get number of players """
        return self.num_players

    def create_players(self):
        """ Function creates players """
        for _ in range(0, self.num_players):
            self.player_list.append(Player())

    def get_player_info(self):
        """ Function get the player(s) information """
        for i in range(0, self.num_players):
            prompt = f'Player {i+1}, enter your name: '
            name = input(prompt)
            input(f'Welcome {name}! Press enter to roll the die for ordering.')
            roll = self.die.roll()
            time.sleep(1)
            print(f'{name} rolled a {roll}! \n')
            self.player_list[i].set_name(name)
            self.player_list[i].set_order(roll)
            time.sleep(1)

    def create_computer(self):
        """ Function creates computer """
        print('Creating computer...')
        time.sleep(2)
        self.player_list.append(Player(human_player=False))
        print('Computer has been created! Computer will roll for ordering.')
        time.sleep(1)
        roll = self.die.roll()
        time.sleep(1)
        print(f'The computer rolled a {roll}! \n')
        self.player_list[-1].set_order(roll)

    def sort_order(self):
        """ Function sorts the players in order """
        self.player_list.sort()

    def play(self):
        """ Function starts and play the game """
        print('Time to play the Pig game! \n')
        time.sleep(2)
        while not self.end:
            for player in self.player_list:
                if player.is_human:
                    player.player_turn()
                else:
                    if self.player_list.index(player) == 0:
                        player.comp_turn(self.player_list[1])
                    else:
                        player.comp_turn(self.player_list[0])
                if player.get_total_score() >= 100:
                    self.end = True
