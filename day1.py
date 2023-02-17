#EXCERTISE 1 Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function
#Write your code below this line 👇 

print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

#EXCERTISE 2  Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


#EXCERTISE 3
#Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

#Write your code below this line 👇
a = input('What is your name? ')
print(len(a))

#EXCERTISE 4  Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a = b
b = temp 


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#BAND GENERATOR

#1. Create a greeting for your program.
print('Welcome')
#2. Ask the user for the city that they grew up in.
a= input('Enter city u grow up in')
#3. Ask the user for the name of a pet.
b=input('enter pet name')
#4. Combine the name of their city and pet and show them their band name.
print(a+b+"\n")
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end





