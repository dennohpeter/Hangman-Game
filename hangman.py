# Python Program to illustrate
# Hangman Game
import random
from collections import Counter


defaults = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

defaults = defaults.split()
 #randomly choose  a secret word from the defaults
word = random.choice(defaults)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()
    playing = True
    # list for storing the letters guessed by the player
    lettersGuessed = ''
    chances = len(word) + 2
    correct = 0
    try:
        while (chances!=0):
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter')
                continue
            # Validation of the guess
            if not guess.isalpha():
               print('Enter only a LETTER!')
               continue
            elif len(guess) > 1:
               print('Enter only a SINGLE letter')
               continue
            elif guess in lettersGuessed:
               print("You have already guessed that letter")

            # if letter is guessed correctly
            if guess in word:
               lettersGuessed += guess

           # printing the word
            for char in word:
               if char in lettersGuessed:
                   print(char, end=' ')
                   correct +=1
               else:
                   print('_', end=' ')
            if (Counter(lettersGuessed) == Counter(word)):
               print()
               print('Congratulations, You won!')
               break
            # if user has used all of his chances
            if chances == 0:
               print()
               print('You lost !! Try again ...')
               print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print("Bye! Try Again.")
        exit()
        # print(letterGuessed)
