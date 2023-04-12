#day 8
#TODO-1: Import and print the logo from art.py when the program starts.

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
import string 
text = input('enter a msg')
#remove white space from a string
text = text.replace(" ","")
cypherText = ''

alphabet = list(string.ascii_letters)
shift = int(input("type the shift number"))
def encrypt(plainText, shiftAmount):
    cypherText = ''
    for letter in plainText:
        position = alphabet.index(letter)
        newPos = position + shiftAmount
        newLetter = alphabet[newPos]
        cypherText += newLetter
    print(f"the cyphered text is {cypherText}")
    
encrypt(text,shift)
#TODO-5: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(cypherText,-4)
#TODO-2: Create a list of the alphabet from a-z. Then, create a variable called 'shift' that takes the user input of how many letters they want to shift their message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-3: Make a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
#TODO-6: Make a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cypher_text, shift_amount):
    plain_text =""
    for letter in cypher_text:
        position = alphabet.index(letter)
        old_position = position - shift_amount
        cipher_text -= alphabet[old_position]
    print(f"The decoded text is {plain_text}")
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt AND decrypt a message.
if direction==("encode"):
    encrypt(plain_text=text, shift_amount=shift)

elif direction=="decode":
    decrypt(cypher_text=text, shift_amount=shift )

else:
    print("Wrong input")

#TODO-7: Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount and print the decrypted text.

#TODO-8: Call the decrypt function and pass in the user inputs. You should be able to test the code and decrypt a message.
is_continue = True
def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    while is_continue:
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {cipher_direction}d result: {end_text}")
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if result == 'No':
        is_continue=True
    else:
        is_continue=False
    
    
    
    