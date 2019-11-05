# !usr/bin/env python3
# *-* coding:utf-8 *-*

all_bdays= {'Noé':'17 dec', 'Clelia':'6 mai'}

def birthdays():
    try:
        while True:
            print('Who\'s birthday are you looking for ?' +\
            '(Blank to quit.)')
            name = input()

            if name == '':
                break

            if name in all_bdays:
                print(name + '\'s birthday is the '+ all_bdays[name])
            else:
                print('Sorry but we do not know the birthday of '+name)
                print('When is it ?')
                bdday = input()
                all_bdays[name] = bdday
                print('Database updated.')
                print(all_bdays)
    except:
        print('An error occured.')

if __name__ == '__main__':
    birthdays()
    print('Programm exit.')