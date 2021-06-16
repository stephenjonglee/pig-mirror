### Stephen Lee
### CPSC 386-01
### stephenjonglee@csu.fullerton.edu

# Pig Game

## Game Description
Die game with 1-4 players. In single player, you will play against a computer. Otherwise, you will play against each other. The game is free-for-all format. The goal of the game is to reach 100 or more points first. Computer will automatically playing their rounds. Terminal game so players just need to type and enter.

## Game requirements
* Python3
* Terminal
* Keyboard

## Gameplay
Every turn, the player have two options (you must type it in the terminal when prompted):
1. 'roll' - roll the die to gain turn points
2. 'hold' - end your turn and gain your turn points
Read the rules for more details.

## Rules
The order of the players will be decided by a die roll (ascending order so lowest roll will go first). Tie breakers are decided by the computer automatically. Players will be prompted to hold or roll. Make sure to spell correctly and all lower-case. If the player rolls a 1, then the player will lose their turn and gain no points. If the player rolls any other number, then the player can decide to keep rolling or hold. If the player decides to hold, then the player will gain that many turn points. The first player to reach 100 points or more will win.

## Computer-Algorithm
The computer has a simple algorithm. It will always roll first. After that, it will calculate if it's total score will be greater than the player's. If it will, then it will hold. Otherwise, it will keep rolling and try to get ahead of the player.

## Known bug
Becareful of typos. The program is designed to check for user input and matching it against 'hold'. If misspelled or capitalized, then the player will not hold and will roll. If the player types 'Hold', then the player will roll.
