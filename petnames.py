
#!/usr/bin/env python3
#*-* coding: utf-8
 
list_of_pets = ['Nuggets', 'Filou', 'Canne']

def petnames():
    print('What pet are you looking for ?')
    name_written = input()
    if name_written in list_of_pets:
        print(name_written + ' is in the list !')
    elif name_written == '':
        print('No name? Well, bye.')
    else:
        print('Sorry, but '+name_written+' is not here...')
    

if __name__ == '__main__':
    petnames()