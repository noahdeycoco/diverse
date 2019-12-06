# /usr/bin/env python3
# coding = utf-8

import os
import shelve

# print(os.path.join('usr', 'home', 'spam'))
# print(os.getcwd())
# os.chdir(os.path.join('..', '..', '..', 'Desktop'))

# try:
#     os.makedirs('test')
# except Exception:
#     Exception

# os.path.realpath()

# aa = open('test.txt', 'a')
# aa.write('\n quatre')
# aa.close()
# content = open('test.txt')
# print(content.read())

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

print(shelfFile)
print(shelfFile['cats'])
print(list(shelfFile.values()))