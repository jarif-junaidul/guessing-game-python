import random

comGuess = random.randint(1, 10)

guessLimit = 3
guessStart = 0

print('Guess a number between 1 to 10')

while guessStart != guessLimit:

    guessRemains = guessLimit - guessStart

    userGuess = int(input(str(guessRemains) + ' guess(es) remain ==> '))

    if userGuess == comGuess:
        print('You win, the number was' + str(comGuess))
        break
    elif userGuess > comGuess:
        print('High, guess lower!')
    else:
        print('Low, guess higher!')

    guessStart += 1

print('Game Over!, the number was ' + str(comGuess))