#day 14 
from database import data
from os import system
import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
#display the art
print(logo)
current_score = 0
def check_answer(guess, a_follower_count, b_follower_count):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:    
    #generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    #format account data into printable format: name, description and country.
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # ask for the user a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    isCorrect = check_answer(guess, a_follower_count, b_follower_count)
    if isCorrect:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        system("clear")
        print(logo)

    elif not isCorrect:
        print(f"You're wrong! current score: {current_score}")
        game_should_continue = False
        






