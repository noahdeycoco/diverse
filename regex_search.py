"""Regex Search
Write a program that opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression. The results should be printed
to the screen.
"""

import random
import os
import re

random_file_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minimveniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def write_initial_file():
    try:
        random_file_text_1 = open('data' + os.sep + 'initial.txt', 'w')
        random_file_text_1.write(random_file_text)
        random_file_text_1.close()
        random_file_text_2 = open('data' + os.sep + 'initial.txt', 'r')
        print(str(len(random_file_text_2.readlines())) 
              + ' line(s) has been writen to initial.txt.')
    except Exception:
        print('An error occured: ' + str(Exception))


def create_data(text):
    try:
        files_text_data = {}
        for i in range(4):
            files_text_data['text_data_%s' % i] = list()
            for _ in range(15):
                text_word = random.choice(text.split())
                files_text_data['text_data_%s' % i].append(text_word)
        return files_text_data
    except Exception:
        print('An error occured: ' + str(Exception))


def write_files():
    try:
        for i in range(4):
            random_file_text_1 = open('data' + os.sep + 'random_text_%s.txt' % i, 'w')
            random_file_text_1.write(' '.join(create_data(random_file_text)['text_data_%s' % i]))
            print(str(os.path.abspath('data' + os.sep + 'random_text_%s.txt' % i)) + ' has been created.')
    except Exception:
        print('An error occured: ' + str(Exception))

def search_regex():
    for _ range():


if __name__ == '__main__':
    write_initial_file()
    create_data(random_file_text)
    write_files()
