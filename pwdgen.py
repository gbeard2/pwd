import random
import math
import array
from english_words import english_words_set

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWER_CASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                         'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                         'y', 'z']

UPPER_CASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                         'Y', 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '!', '_']

CHAR_TO_SYMBOL = {'a': '@', 'A': '4', 's': '$', 'S': '5',
                  'i': '1', 'e': '3', 'E': '3', 'o': '0', 'O': '0'}


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


def generateRandomizedPassword():
    password, characterChoices, length = getInput()

    currentLength = len(password)
    for i in range(length - currentLength):
        password.append(random.choice(characterChoices))
        random.shuffle(password)

    return ''.join(password)


def generateRandomWordPassword():
    desiredLength = int(
        input('Desired Password Length (enter 0 if unwanted): '))
    wordCount = int(input('Enter Number of Words (1 minimum): '))
    replaceWithSymbols = input(
        'Replace Letters With Look-a-Like Symbol/Digit (y/n): ')
    randomCasing = input('Randomly Capitalize(y/n): ')

    password = []
    wordSet = english_words_set
    wordLengthLimit = math.ceil(float(desiredLength) / float(wordCount))

    if(wordLengthLimit <= 1 and desiredLength):
        print("The given length and number of words does not allow for password",
              "generation. Please increase the length or decrease the word count")
        return
    if(wordCount > 1 and desiredLength):
        wordLength = wordLengthLimit
        wordSet = trimDictionary(english_words_set, wordLength)

    for i in range(wordCount):
        if(desiredLength > 0 and i is wordCount - 1):
            remainingCharacters = desiredLength - len(''.join(password))
            sortedSet = trimDictionary(english_words_set, remainingCharacters)
            randomWord = random.sample(sortedSet, 1)[0]
        else:
            randomWord = random.sample(wordSet, 1)[0]

        if(includeSetting(replaceWithSymbols)):
            randomWord = replaceWithSymbol(randomWord)
        if(includeSetting(randomCasing)):
            randomWord = ''.join(random.choice(
                (str.upper, str.lower))(c) for c in randomWord)

        password.append(randomWord)
    return ''.join(password)


def replaceWithSymbol(word):
    temp = list(word)
    for i in range(len(temp)):
        if(temp[i] in CHAR_TO_SYMBOL):
            temp[i] = CHAR_TO_SYMBOL[temp[i]]
    return ''.join(temp)


def trimDictionary(words, length):
    sortedWords = sorted(words, key=len)
    i = start = end = 0
    for word in sortedWords:
        if(len(word) == length and start == 0):
            start = i
        if(len(word) > length):
            end = i - 1
            break
        i += 1
    return sortedWords[start:end]


if __name__ == '__main__':
    # print(generateRandomizedPassword())
    print(generateRandomWordPassword())
