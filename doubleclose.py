import sys
import random
playing = True
numRan = random.randint(1, 10)
weirdLol = (0.1+0.2)
if weirdLol == 0.30000000000000004:
    weirdLol = 0.3
print(weirdLol)
print("Playing random number guessing game!")


while playing:
    p1Guess = int(input("Player 1 enter your guess! \n"))
    p2Guess = int(input("Player 2 enter your guess! \n"))

    if p1Guess > 10:
        print("ERR: GUESS OVER MAX")
        sys.exit()
    if p2Guess > 10:
        print("ERR: GUESS OVER MAX")
        sys.exit()
    if p1Guess < numRan:
        print('Player 1 Guess is under!')
    if p1Guess > numRan:
        print('Player 1 Guess is over!')
    if p1Guess == numRan:
        print('Player 1 got it!')
    if p2Guess < numRan:
        print('Player 2 Guess is under!')
    if p2Guess > numRan:
        print('Player 2 Guess is over!')
    if p2Guess == numRan:
        print('Player 2 got it!')
