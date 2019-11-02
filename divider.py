#!/usr/bin/env python3
#*-* coding: utf-8

import random

def selected_number():
    global user_number
    user_number = ''
    try:
        print('Choose a number which 10 will divide.')
        user_number = int(input())
    except Exception as e:
        print(e)

def divide(user_number):
    try:
        result = 10/user_number
        print('10/'+str(user_number)+ ' = ' + str(result))
    except ZeroDivisionError:
        print('You can\'t divide by zero.')
    except TypeError:
        print('Please enter a correct number.')

if __name__ == '__main__':
    selected_number()
    divide(user_number)
