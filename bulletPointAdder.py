# /usr/bin/env python3
# coding:utf_8

import pyperclip
# import sys


def intro():
    print(' BULLET POINT ADDER '.center(45, '*'))
    print('What was in  your clipboard is now a list !')
    # print('\nEnter a key to continue. \nEnter "q" to exit.')
    # user_choise = input()
    # try:
    #     if user_choise != 'q':
    #         pass
    #     else:
    #         print('Exit programm.')
    #         sys.exit()
    # except SystemExit:
    #     pass


def list_clipboarded():
    clipboard = pyperclip.paste()
    list_transformed = []
    [list_transformed.append('- ' + i) for i in clipboard.splitlines()]
    return '\n'.join(list_transformed)


if __name__ == '__main__':
    intro()
    pyperclip.copy(list_clipboarded())
