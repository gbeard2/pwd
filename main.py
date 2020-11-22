import pwdgen
import pwdtest
import os


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def printMenu(menu, funcs=None):
    """Will print out a dictionary defined menu and ask for a selection when given a list of functions"""
    for key, value in menu.items():
        print(key + ': ' + value)

    if funcs is not None:
        flag = True
        while flag:
            choice = input('Choice: ')
            try:
                funcs[choice]['func'](**funcs[choice]['args'])
            except KeyError:
                print('Invalid choice! Try again.')
            else:
                flag = False
    return


TEST_MENU = {'1': 'Brute Force',
             '2': 'Dictionary Attack',
             '3': 'Return'}

TEST_MENU_FUNCTIONS = {'1': {'func': pwdtest.bruteForce, 'args': {}},
                       '2': {'func': type(None), 'args': {}},
                       '3': {'func': type(None), 'args': {}}}

MAIN_MENU = {'1': 'Generate Password',
             '2': 'Test Password',
             '3': 'Exit'}

MAIN_MENU_FUNCTIONS = {'1': {'func': type(None), 'args': {}},
                       '2': {'func': printMenu, 'args': {'menu': TEST_MENU, 'funcs': TEST_MENU_FUNCTIONS}},
                       '3': {'func': exit, 'args': {}}}

if __name__ == '__main__':
    while True:
        printMenu(MAIN_MENU, funcs=MAIN_MENU_FUNCTIONS)
        clear()
