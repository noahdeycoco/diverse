# hotkeys

# /usr/bin/env python3
# coding:utf_8

import pyperclip
import sys

def intro(): # ajouter un try
    print(' HOTKEYS '.center(45, '*'))
    print('(L)ines grouped \n(C)olumns group')
    print('(M)ultiplier effect \n(E)nding year')
    user_input = input("Please select ")
    if user_input.lower() == 'l':
        group_columns_values_for_each_line()
    elif user_input.lower() == 'c':
        group_columns_values_for_each_columns()
    elif user_input.lower() == 'm':
        nb = input('How many times?')
        multiplier_effect(nb)
    elif user_input.lower() == 'e':
        nb = input('How many times?')
        ending_year(nb)
    else:
        print('exit')
        sys.exit()


def group_columns_values_for_each_line():
    print(' GROUP COLUMNS VALUES FOR EACH LINE '.center(45, '*'))
    clipboard = pyperclip.paste()
    print(clipboard)
    data = [line.split('\t') for line in clipboard.splitlines()]
    master_list = []

    for i in range(len(data[0])):
        master_list.append((list(zip(*data))[i]))

    flat_list = [item for sublist in master_list for item in sublist]
    print(master_list)
    return pyperclip.copy('\n'.join(flat_list))
    

def group_columns_values_for_each_columns():
    print(' GROUP COLUMNS VALUES FOR EACH COLUMNS '.center(45, '*'))
    clipboard = pyperclip.paste()
    print(clipboard)
    data = [line.split('\t') for line in clipboard.splitlines()]
    flat_list = [item for sublist in data for item in sublist]
    print(flat_list)
    return pyperclip.copy('\n'.join(flat_list))

def multiplier_effect(nb):
    print(' MULTIPLIER EFFECT '.center(45, '*'))
    clipboard = pyperclip.paste()
    list_transformed = clipboard.splitlines()
    list_transformed = list_transformed*int(nb)
    list_transformed = '\n'.join(list_transformed)
    print(list_transformed)
    return pyperclip.copy(list_transformed)

def ending_year(nb):
    print(' ENDING YEAR '.center(45, '*'))
    clipboard = pyperclip.paste()
    print(clipboard)
    list_transformed = []
    [list_transformed.insert(0, str("31-12-"+i)) for i in clipboard.splitlines()]
    list_transformed = list_transformed*int(nb)
    list_transformed.sort()
    list_transformed = '\n'.join(list_transformed)
    print(list_transformed)
    return pyperclip.copy(list_transformed)


if __name__ == '__main__':
    intro()