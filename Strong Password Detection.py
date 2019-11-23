# /usr/bin/env python3
# coding=utf-8


# Write a function that uses regular expressions to make sure the password string
# it is passed is strong. A strong password is defined as one that is at least 
# eight characters long, contains both uppercase and lowercase characters, and 
# has at least one digit. You may need to test the string against multiple regex
# patterns to validate its strength.

import re

strong_password_regex = re.compile(r'''
\w{8,} # 8 characters at least
[a-zA-Z] # uppercase and lowercase
\d+ # at least one digit
''', re.VERBOSE())

def strong_password_checker():



if __name__ == '__main__':
    strong_password_checker()