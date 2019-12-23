"""Regex Search
Write a program that opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression. The results should be printed
to the screen.
"""


import random

random_file_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


import random
import string
import os

initial_t = os.open(('data' + os.sep + 'intial.txt'), 'r')
pritn(initial_t.readline())

# print(random_file_text.split('\n'))

# for i in range(4):
#     random.shuffle(random_file_text.split('\n'))
#     print(random_file_text[0:4])