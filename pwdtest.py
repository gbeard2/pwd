import time

START_SPECIAL_CHAR = 33
START_NUMBER = 48
START_TEXT = 65
END_TEXT = 122


def bruteForce():
    password = input('Enter password: ')
    start = time.process_time()
    password = list(password)
    found = False
    char_count = 1
    current_char = START_SPECIAL_CHAR
    guess = []
    while not found:
        for pos in range(0, char_count):
            while current_char <= END_TEXT:
                try:
                    try:
                        guess[pos] = current_char
                    except IndexError:
                        guess.append(current_char)
                    assert guess == password
                except AssertionError:
                    current_char += 1
                else:
                    found = True
    print('Time to crack: ' + str(time.process_time() - start))
