#!/usr/bin/env python3
""" Pig Game - Main File """

__author__ = 'Stephen Lee'
__email__ = 'stephenjonglee@csu.fullerton.edu'
__maintainer__ = 'stephenjonglee'

import time
from pig import Pig


def main():
    """ The main function of the program """
    intro()
    num = get_num_players()
    print(f'There are {num} players. \n')
    game = Pig(num=num)
    run(game)
    end()


def intro():
    """ Displays a greeting for the game """
    print("Hello! Welcome to the Pig Game! \n")
    time.sleep(1)


def get_num_players():
    """ Function get the number of players """
    prompt = 'Enter the number of players (1-4): '
    num = int(input(prompt))
    while num not in range(1, 5):
        print('Error. Incorrect number of players. Please try again. \n')
        num = int(input('Enter the number of players (1-4): '))
    return num


def run(game):
    """ Function set up the game """
    game.create_players()
    game.get_player_info()
    if game.get_num_players() == 1:
        game.create_computer()
    game.sort_order()
    game.play()


def end():
    """ Displays the conclusion of the program """
    print("Thanks for playing!")
    time.sleep(2)
    print("Come back for more later!")
    time.sleep(2)
    print("Goodbye!")
    time.sleep(2)


if __name__ == '__main__':
    main()
