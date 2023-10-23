"""Program that will loop until the correct number is guessed"""
from random import randint
number: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
guesses = 0
while number != guess:
    if guess < number:
        print('too low')
    else:
        print('too high')
    number: int = randint(0,10)
    print('nope')
    guess: int = int(input("Guess a number between 1 and 10: "))
    guesses+=1
#by this point, while loop is exited and guess = number
print('got it')
print(guesses)
