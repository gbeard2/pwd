import time

START_CHAR = 65
END_CHAR = 122


def bruteForce():
    password = input('Enter password: ')
    start = time.process_time()
    password = list(password)
    char_count = len(password)
    guess = []
    for i in range(0, char_count):
        guess.append(chr(START_CHAR))
    while True:
        for i in range(START_CHAR, END_CHAR + 1):
            try:
                assert guess == password
            except AssertionError:
                guess[0] = chr(i)
            else:
                break
        try:
            assert guess == password
        except AssertionError:
            for pos, char in enumerate(guess):
                if ord(char) == END_CHAR:
                    try:
                        guess[pos] = chr(START_CHAR)
                        guess[pos + 1] = chr(ord(guess[pos + 1]) + 1)
                    except IndexError:
                        print('Failed to crack.')
                        return
        else:
            break
    print('Guess: ' + ''.join(guess))
    print('Time to crack: ' + str(time.process_time() - start) + ' seconds')
    return
