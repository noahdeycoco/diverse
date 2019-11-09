# usr/bin/env/ python3
# *-* coding:utf-8 *-*

# import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('This is ' + turn + '. Where do you want to play ?')
    play = input()
    theBoard[play] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
