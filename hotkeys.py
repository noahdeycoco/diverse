# hotkeys

# /usr/bin/env python3
# coding:utf_8

import pyperclip
import sys

def intro(): # ajouter un try
    print(' HOTKEYS '.center(45, '*'))
    print('(D)ata list \n(M)ultiplier effect')
    # user_input = input('>')
    user_input = 'D'
    if user_input.lower() == 'd':
        print('DEBUTANNE+FINANNEE+TIMES')
        print('DEBUTANNE')
        # debutannee_input = input('INPUT YEAR (YYYY)')
        # finannee_output = input('OUTPUT YEAR (YYYY)')
        # times_input = input('TIMES (int)')
        debutannee_input = 2000
        finannee_output=2003
        times_input = 3
        for i in range(times_input):
            s='-'
            debutannee= "31-12-"+str(debutannee_input)
            print(debutannee)
        for i in range(times_input):
            s='-'
            finannee= "31-12-"+str(finannee_output)
            print(finannee)
        
        print('LISTE ANNEE')
        clipboard = pyperclip.paste()
        list_transformed = []
        [list_transformed.append('- ' + i) for i in clipboard.splitlines()] 



    elif user_input.lower() == 'M':
        print(4)
    else:
        print('exit')
        sys.exit()

def list_clipboarded():
    clipboard = pyperclip.paste()
    list_transformed = []
    [list_transformed.append('- ' + i) for i in clipboard.splitlines()]
    return '\n'.join(list_transformed)


if __name__ == '__main__':
    intro()
    # pyperclip.copy(list_clipboarded())