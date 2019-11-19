# /usr/bin/env python3
# coding:utf-8

import re

my_regex = re.compile(r'(va)+ (\d,\d)?')
sentence = my_regex.findall('Bonjour2,3 comment ça vava 4,5 va 4,5 va 4,5')

try:
    print(sentence)
    print(type(sentence))
    print(sentence.group())
    print(sentence.group(2))
except Exception:
    print('error')
    pass


dinner_reg = re.compile(r'<.*?>')
dinner_sentenece = dinner_reg.search('<It is very nice> especially the'
                                     'sauce on the top.>')

print(dinner_sentenece.group())

secret_reg= re.compile('Agent \w+')
secret_sentence = 'Agent Kim is in love with Agent Catherine !'
print(secret_reg.sub('X', secret_sentence))
