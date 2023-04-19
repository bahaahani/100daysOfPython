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
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        


def game():
    #choose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    print(f"Pssst, the correct answer is {answer}")
    guess = 0
    while guess != answer:
        print("Make a guess: ")
        guess = int(input())        
        turns = check_answer(guess, answer, turns)
        print(f"you have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guess != answer:
            print("Guess again.")
            
game()