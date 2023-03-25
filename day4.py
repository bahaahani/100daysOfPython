import random

num = random.randint(1, 3)
print(num)

# day4
## head tail game
headTail = input("Heads or Tails? ")
rand= random.randint(0, 1)
if rand == 0:
    print("Tails")
else:
    print("Heads")
    
if headTail == "Heads" and rand == 1:
    print("You win!")   

list = ["Heads", "Tails"]
fruit = random.choice(list)
sates_of_america = ['Deleware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire',
'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois',
'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia',
'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

states = random.choice(sates_of_america)
print(states)
#who is going to pay the bill game

str = input('who is going to pay the bill?').split(',')
choice = random.choice(str)
print(f'{choice} you are going to pay the bill')

#treasure map game
print('welcome to treasure island')

print('your mission is to find the treasure')


#rock paper scissors game

rock_paper_scissors = input("Rock, Paper, Scissors? ").lower()
rand = random.randint(0, 2)
if rand == 0:
    print("Rock")
elif rand == 1:
    print("Paper")
else:
    print("Scissors")

if rock_paper_scissors == "rock" and rand == 0:
    print("Draw")
elif rock_paper_scissors == "rock" and rand == 1:
    print("You lose")
elif rock_paper_scissors == "rock" and rand == 2:
    print("You win")
elif rock_paper_scissors == "paper" and rand == 0:
    print("You win")
elif rock_paper_scissors == "paper" and rand == 1:
    print("Draw")
elif rock_paper_scissors == "paper" and rand == 2:
    print("You lose")
elif rock_paper_scissors == "scissors" and rand == 0:
    print("You lose")
elif rock_paper_scissors == "scissors" and rand == 1:
    print("You win")
elif rock_paper_scissors == "scissors" and rand == 2:
    print("Draw")

#password generator game
password = ""
for i in range(0, 3):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+")

print(password)

import random

# Password Generator Project
password = ""
for i in range(0, 3):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+")
print(password)

# EASY: Letters + Numbers
# MEDIUM: Letters + Numbers + Symbols
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for i in range(0, nr_letters):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(0, nr_symbols):
    password += random.choice("!@#$%^&*()_+")
for i in range(0, nr_numbers):
    password += random.choice("1234567890")
print(password)


# HARD: Letters + Numbers + Symbols

 