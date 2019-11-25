# /usr/bin/env python3
# coding=utf-8

import re
import sys

strong_password_regex = re.compile(r'''
\w{8,}      # 8 characters at least
[a-zA-Z]    # uppercase and lowercase
\d+         # at least one digit
''', re.VERBOSE)


def user_input():
    global user_password
    try:
        print('Enter a strong password with at least eight characters,'
              'uppercase and lowercase characters, and at least one digit.')
        user_password = str(input())
    except Exception:
        print('An error occured in user_input : ' + str(Exception))


def strong_password_checker():
    try:
        match_pass = strong_password_regex.search(user_password)
        match_result = match_pass.group()
        print('Congratulations, ' + str(match_result) +
              ' is a strong password !')
    except AttributeError:
        print('Your password do not respect minimal conditions : '
              + str(AttributeError))


def programm_exit():
    sys.exit('Programm exit.')


if __name__ == '__main__':
    user_input()
    strong_password_checker()
    programm_exit()
