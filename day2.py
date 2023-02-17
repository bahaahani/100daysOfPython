# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
x = two_digit_number[0]
y = two_digit_number[1]
result = str(int(x) + int(y))

#print(x +'+'+ y  + '=' + result )
# print(x+y)
first_number = two_digit_number[0]
second_number = two_digit_number[1]

result = int(first_number) + int(second_number)
print (first_number + " " + "+" + " " + second_number )
print(result)

#EXCERCISE 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(int(float(weight) / float(height) ** 2))

# EXCERCISE 3

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

r = f"you have {days} days {weeks} weeks {months} months"
print(r)

# TIP CALCULATOR

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator.')
t= float(input('What was the total bill?'))
i= float(input('What percentage tip would you like to give? 10, 12, or 15?'))
p = int(input('How many people to split the bill?'))

r = (t/p) * (1+i/100)
r = round(r)

print(f'Each person should pay: ${r} ')



