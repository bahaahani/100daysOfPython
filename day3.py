#EX 1 ODD EVEN
x= int(input('enter a number'))
if x % 2==0:
    print('true')
else:
    print('false')

#EX 2 TICKET SALES REPORT

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input ("What is your age? "))
  if age <= 12:
      print("Please pay $7.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

  #EX 3 BMI WITH CONDITIONS
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")


#EX 4 LEAP YEAR CALCULATOR
year = int(input('enter a year'))
#Write your code below this line
if year % 4 == 0:
  if year % 100 ==0:
    if year % 400 ==0:
      print("Leap year")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
  
# EX 5 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
  
# PIZZA DELIVERY 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

# LOVE CALCULATOR 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


