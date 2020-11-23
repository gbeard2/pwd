import time
import hashlib
import requests

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

CHAR_SETS = [DIGITS, LOWER_CASE_CHARACTERS, UPPER_CASE_CHARACTERS, SYMBOLS]


def charCheck(password):
    potential_chars = []
    for char_set in CHAR_SETS:
        for char in char_set:
            if password.find(char) != -1:
                potential_chars += char_set
                break
    potential_chars.append('NULL')
    return potential_chars


def bruteForce():
    password = input('Enter password: ')
    potential_chars = charCheck(password)
    start = time.process_time()
    password = list(password)
    char_count = len(password)
    guess = []
    for i in range(0, char_count):
        guess.append(potential_chars[0])
    while True:
        for i in range(1, len(potential_chars)):
            try:
                assert guess == password
            except AssertionError:
                guess[0] = potential_chars[i]
            else:
                break
        try:
            assert guess == password
        except AssertionError:
            for pos, char in enumerate(guess):
                if char == potential_chars[-1]:
                    try:
                        guess[pos] = potential_chars[0]
                        guess[pos + 1] = potential_chars[potential_chars.index(guess[pos + 1]) + 1]
                    except IndexError:
                        print('Failed to crack.')
                        return
        else:
            break
    print('Guess: ' + ''.join(guess))
    print('Time to crack: ' + str(time.process_time() - start) + ' seconds')
    return


def dictAtk():
    password = input('Enter password: ')
    pass_hash = hashlib.sha1(password.encode('utf-8'))
    pass_hash = pass_hash.hexdigest()
    response = requests.get('https://api.pwnedpasswords.com/range/' + pass_hash[0:5])
    print(response.content)
