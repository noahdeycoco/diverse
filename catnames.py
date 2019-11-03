#!/usr/bin/env python3
#*-* coding: utf-8

def catnames():
    list_of_cats = []
    while True:
        print('What is your cat '+str(len(list_of_cats)+1)+' name ? \n Press nothing to exit.')
        cat_name = input()
        if cat_name == '':
            break
        else:
            list_of_cats.append(cat_name)
    if len(list_of_cats) == 0:
        print('You don\'t have any cat? I feel sorry for you!')
    if len(list_of_cats) == 1:
        print('I\'ll love to meet ' +list_of_cats+ ' one day !')
    if len(list_of_cats) > 1:
        print('What sweet names :')
        for i in list_of_cats:
            print('     - '+i)

def programm_exit():
    print('\n Programm exit.')


if __name__ ==  '__main__':
    catnames()
    programm_exit()