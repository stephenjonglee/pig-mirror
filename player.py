#!/usr/bin/env python3
""" Pig Game - Player Class File """

__author__ = 'Stephen Lee'
__email__ = 'stephenjonglee@csu.fullerton.edu'
__maintainer__ = 'stephenjonglee'

import time
from die import Die


class Player:
    """ Class PLayer """
    def __init__(self, human_player=True):
        self.is_human = human_player
        if self.is_human:
            self.name = 'Player'
        else:
            self.name = 'Computer'
        self.order = 0
        self.total_score = 0
        self.turn_score = 0
        self.count = 0
        self.die = Die()

    def __str__(self):
        """ Function return Player class as a string """
        return f'Player: {self.name} \n' \
               f'Total Score: {self.total_score} \n' \
               f'Current turn score: {self.turn_score} \n' \
               f'Number of rolls: {self.count} \n'

    def __lt__(self, other):
        """ Function less than to sort Player class """
        return self.order < other.order

    def get_name(self):
        """ Function get name of player """
        return self.name

    def set_name(self, title):
        """ Function sets the name of player """
        self.name = title

    def set_order(self, num):
        """ Function sets the order roll of the player """
        self.order = num

    def check_is_human(self):
        """ Function checks if player is human """
        return self.is_human

    def get_total_score(self):
        """ Function get the total score of the player """
        return self.total_score

    def player_turn(self):
        """ Function for a player turn """
        print(self)
        prompt = f'{self.name}, would you like to roll or hold? '
        hold = input(prompt) == 'hold'
        while not hold:
            roll = self.die.roll()
            print(f'You rolled a {roll}. \n')
            time.sleep(1)
            if roll != 1:
                self.turn_score += roll
                self.count += 1
                print(self)
                prompt = f'Keep rolling or hold? '
                hold = input(prompt) == 'hold'
            else:
                self.turn_score = 0
                hold = True
                print(f'Oh no! Since you rolled a 1, you gain no points.')
                time.sleep(1)
        print(f'{self.name} turn is over. You have gained {self.turn_score} points.')
        time.sleep(1)
        self.total_score += self.turn_score
        print(f'Total score for {self.name} is {self.total_score}. \n')
        if self.total_score >= 100:
            print(f'Congratulations {self.name}! You are the winner! \n')
            time.sleep(2)
        self.turn_score = 0
        self.count = 0
        time.sleep(2)

    def comp_turn(self, player):
        """ Function for a computer turn """
        temp_total = self.total_score
        less_than_player = True
        print(self)
        time.sleep(2)
        while less_than_player:
            print('Computer will roll.')
            time.sleep(2)
            roll = self.die.roll()
            print(f'The computer rolled a {roll}. \n')
            time.sleep(1)
            if roll != 1:
                self.turn_score += roll
                self.count += 1
                print(self)
                temp_total += self.turn_score
                print('Computer is thinking...')
                time.sleep(2)
                if temp_total > player.total_score:
                    print('Computer will hold.')
                    less_than_player = False
            else:
                self.turn_score = 0
                print(f'Oh no! Since the computer rolled a 1, it gains no points.')
                less_than_player = False
                time.sleep(2)
        print(f'{self.name} turn is over and gained {self.turn_score} points.')
        time.sleep(1)
        self.total_score += self.turn_score
        print(f'Computer total score is {self.total_score} \n')
        if self.total_score >= 100:
            print(f'Sorry, {self.name} is the winner. You will win next time! \n')
        time.sleep(2)
        self.turn_score = 0
        self.count = 0
