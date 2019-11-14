# /usr/bin/env python3
# coding:utf-8

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

new_table_data = []


def printTable():
    for y in range(len(tableData[0])):  # 4
        for i in range(len(tableData)):  # 3
            new_table_data.append(tableData[i][y])
    # print(new_table_data)
    for z in range(len(tableData[0])):
        first = int(0+(len(tableData)*z))
        last = int(3+(len(tableData)*z))
        print(' '.join(new_table_data[first:last]).rjust(20))


printTable()
