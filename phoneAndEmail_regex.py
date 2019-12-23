# /usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re
import sys

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

frenchPhoneRegex = re.compile(r'''(
(\+\d{2}(\s|-|\.))? # extension code
(\d{1,2})
(\s|-|\.)?
(\d{2})
(\s|-|\.)?
(\d{2})w
(\s|-|\.)?
(\d{2})
(\s|-|\.)?
(\d{2})
)''', re.VERBOSE)

# mailRegex_old = re.compile(r'\w+@\S*\.\w+')  # Need to forbid special carac
mailRegex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


def find_email(source):
    # print(str(type(source)) + ': ' + str(source))
    findall_results = mailRegex.findall(source)
    # print(findall_results)
    try:
        if len(findall_results) == 1:
            print('One email has been found and has been copied to clipboard:')
            print(''.join(findall_results))
            pyperclip.copy(''.join(findall_results))
        elif findall_results == []:
            print('No email address has been found from the source.')
        else:
            # print(findall_results)
            print('Email adresses has been found and copied to clipboard.')
            pyperclip.copy('\t'.join(findall_results))
    except Exception:
        print('An error occured: ' + str(Exception))


def programm_exit():
    try:
        sys.exit('Programm exit.')
    except Exception:
        print('An error occured when trying to exit: ' + str(Exception))


if __name__ == '__main__':
    find_email(pyperclip.paste())
    programm_exit()
