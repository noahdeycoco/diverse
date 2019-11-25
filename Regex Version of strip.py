# /usr/bin/env python3
# coding=utf-8

# Write a function that takes a string and does the same thing as the strip() 
# string method. If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the 
# string. Otherwise, the characters specified in the second argument to the 
# function will be removed from the string.

# /usr/bin/env python3
# coding=utf-8

import re
import sys


regex_strip_white_space = re.compile(r'''
\S+         # Match any non-whitespace character
(\s{1}\S+)* # Match one space between words' string
''', re.VERBOSE)


# TODO: Run script when user_strip has no value


# user_strip = None

# regex_strip_user = re.compile(
# r'[^' + re.escape(user_strip) + r']'  # matche variable
# + r'\S+'
# + r'(\s{1}\S+)*'
# + r'[^' + re.escape(user_strip) + r']') # [^0]

# user_string = '   20a0a02 2 '
# # print("Enter charcaters to strip if you want to.")
# # user_strip = str(input()))


# def regex_streapteaser(regex_strip_white_space):
#     try:
#         if user_string == None:
#             white_space_stripped = regex_strip_white_space.search(user_string)
#             print(white_space_stripped.group())
#             print(len(white_space_stripped.group()))
#             print(1)
#         else:
#             user_string_stripped = regex_strip_user.search(user_string)
#             print(user_string_stripped.group())
#             print(2)
#     except Exception:
#         print(Exception)


# if __name__ == '__main__':
#     regex_streapteaser(regex_strip_white_space)

