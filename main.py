import pwdgen
import pwdtest


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


GEN_MENU = {'1': 'Random',
            '2': 'Set of Words',
            '3': 'Return'}

GEN_MENU_FUNCTIONS = {'1': {'func': pwdgen.generateRandomizedPassword, 'args': {}},
                      '2': {'func': pwdgen.generateRandomWordPassword, 'args': {}},
                      '3': {'func': type(None), 'args': {}}}

TEST_MENU = {'1': 'Brute Force',
             '2': 'Dictionary Attack',
             '3': 'Return'}

TEST_MENU_FUNCTIONS = {'1': {'func': pwdtest.bruteForce, 'args': {}},
                       '2': {'func': pwdtest.dictAtk, 'args': {}},
                       '3': {'func': type(None), 'args': {}}}

MAIN_MENU = {'1': 'Generate Password',
             '2': 'Test Password',
             '3': 'Exit'}

MAIN_MENU_FUNCTIONS = {'1': {'func': printMenu, 'args': {'menu': GEN_MENU, 'funcs': GEN_MENU_FUNCTIONS}},
                       '2': {'func': printMenu, 'args': {'menu': TEST_MENU, 'funcs': TEST_MENU_FUNCTIONS}},
                       '3': {'func': exit, 'args': {}}}

if __name__ == '__main__':
    while True:
        printMenu(MAIN_MENU, funcs=MAIN_MENU_FUNCTIONS)
