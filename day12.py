#day 12
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user guess against actual number
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

#choose a random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

print(f"you have {set_difficulty()} attempts remaining to guess the number.")
print(f"Pssst, the correct answer is {answer}")

guess = input("Make a guess: ")
check_answer(guess, answer, set_difficulty())