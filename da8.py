def greet():
    print ("hello students this is dr ali alsaffar")
    print ("welcome to my class itcs255 where i will make  u suffer ")


    # function that allows for input of a number and returns the sum of all numbers from 1 to that number
def greetName(name):
    print ("hello " + name + " welcome to my class itcs255 where i will make  u suffer ")

# function with more than one parameter
def greetName2(name, age):
    print("hello " + name + " welcome to my class itcs255 where i will make  u suffer ")
    print(" you are " + str(age) + " years old")

#positional arguments
greetName2("ali", 25)


# wall painting calculator
height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
cover = 5

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {number_of_cans} cans of paint.")

paint_calc(height, width, cover)

#prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number, 2):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

#ceasar cipher

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
alphabet = "abcdefghijklmnopqrstuvwxyz"
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")
