import random
import array

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWER_CASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

UPPER_CASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')']


def includeSetting(answer):
    return answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes'

def getInput():
    length = int(input('Enter Password Length (4 is lowest): '))
    upperCase = input('Include Uppercase (y/n): ')
    digits = input('Include Digits (y/n): ')
    symbols = input('Include Symbols (y/n): ')
    
    characterChoices = LOWER_CASE_CHARACTERS
    temp_pass = [random.choice(LOWER_CASE_CHARACTERS)]
    
    if(length < 4):
        length = 4
    if(includeSetting(upperCase)):
        characterChoices += UPPER_CASE_CHARACTERS
        temp_pass.append(random.choice(UPPER_CASE_CHARACTERS))
    if(includeSetting(digits)):
        characterChoices += DIGITS
        temp_pass.append(random.choice(DIGITS))
    if(includeSetting(symbols)):
        characterChoices += SYMBOLS
        temp_pass.append(random.choice(SYMBOLS))
    return temp_pass, characterChoices, length 

def generatePassword():
    password, characterChoices, length = getInput()
    
    currentLength = len(password)
    for x in range(length - currentLength):
        password.append(random.choice(characterChoices))
        random.shuffle(password)
        
    return ''.join(password)


if __name__ == '__main__':
    print(generatePassword())
