# /usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''( 
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)


frenchPhoneRegex = re.compile(r'''(
((+)?\d{2})  # area code
\d{}
6 23 84 73 89
09 83 23 32 32
)''', re.VERBOSE)

# TODO: Create email regex.

mailRegex = re.compile(r'\w+@.*\.\w+')
# test
# mailSentence = mailRegex.search('fsq bonjour ds2dq@dq34s. com dqs')
# print(mailSentence.group())

# TODO: Find matches in clipboard text. 
# TODO: Copy results to the clipboard.
