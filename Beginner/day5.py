#day 5 
#for loop
#range function
#range(start, stop, step)
# for i in range(1, 10, 2):
#     print(i)

# for i in range(1, 10):
#     print(i)

students_height = input("Input a list of student heights ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

total_height = 0
for height in students_height:
    total_height += height
print(total_height)

number_of_students = 0
for student in students_height:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

#highest score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#add even numbers
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

#fizzbuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


#forloop to generate a password

import random

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

    #hard level

password = ''
for i in range(0, nr_letters):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(0, nr_symbols):
    password += random.choice("!@#$%^&*()_+")
for i in range(0, nr_numbers):
    password+= random.choice("1234567890")
print(password)
password = list(password)
random.shuffle(password)
print(password)
password = "".append(password)
print(password)

