# Guess the number game from Automate the Boring Stuff from memory
# By Ryan McMillan Dec 2019
# Testing Github Integration in VSCode

import random

TITLE = 'GUESSING GAME'
print(TITLE)
print(len(TITLE) * '-')

print('What is your name?')
name = str(input())

secret_number = random.randint(1, 20)
print('What is your first Guess?')
for guess_number in range(1, 6):
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low..')
    elif guess > secret_number:
        print('Your guess is too high..')
    else:
        # This is if the contestant guesses right. break the loop and continue on
        break

if guess == secret_number:
    print('You win ' + name + '! It took you ' + str(guess_number) + ' guesses')
else:
    print('You Lose! Better luck next time.')
