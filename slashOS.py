# /usr/bin/env python3
# coding = utf-8

import os

print(os.path.join('usr', 'home', 'spam'))
print(os.getcwd())
# os.chdir(os.path.join('..', '..', '..', 'Desktop'))

try:
    os.makedirs('test')
except Exception:
    Exception

os.path.realpath()
 