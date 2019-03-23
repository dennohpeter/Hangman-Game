# Python Program to illustrate
# Hangman Game

import random
from collections import Counter
defaults = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

defaults = defaults.split()
 #randomly choose  a secret word from the defaults
 word = random,choice(defaults)

 if __name__ == '__main__':
     print('Guess the word! HINT: word is a name of a fruit')
     for i in word:
         # For printing the empty spaces for letters of the word
         print('_', end = ' ')
     print()
     playing = True
     # list for storing the letters guessed by the player
     lettersGuessed = ''
     chances = len(word) + 2
     correct = 0
     try:
         
