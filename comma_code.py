#!/usr/bin/env python3
#*-* coding: utf-8

spam = ['apples', 'bananas', 'tofu', 'cats']

def and_ending(my_list):
    try:
        if isinstance(my_list, list):
            sentence = (', '.join(my_list))
            last_char = len(my_list[-1])+2 # nb of characters of the last word
            print(sentence[:-(last_char)] + ' and ' + my_list[-1])
        else:
            print(str(my_list)+ ' is not a list and is detected as a: ' +\
                str(type(my_list)))
    except:
         print('An error occurred.')

if __name__ == '__main__':
    and_ending(spam)