import random

num = random.randint(1, 3)
print(num)

# Path: day4.py
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