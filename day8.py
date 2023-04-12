#day 8
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

encrypt(cypherText,-4)

