alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import Day8_art

def caesar(text, shift, direction):
    cypher = ''
    if direction == 'decode': shift *= -1
    for letter in text: 
        if not letter.isalpha(): 
            cypher += letter
            continue
        cypher += alphabet[alphabet.index(letter) + shift]
    print('The ' + direction + ' message is' + ' ' + cypher)

start = 'yes'
print(Day8_art.logo + '\n')
while (start == 'yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift%26

    caesar(text,shift,direction)

    start = input('Would you like to do another one? Yes/No \n').lower()