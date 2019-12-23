import os

text_to_write = """The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.
The program would find these occurrences and prompt the user to replace them.
"""


def create_dir_and_file():
    try:
        if os.path.isfile('data' + os.sep + 'initial.txt'):
            print('\'data' + os.sep + 'initial.txt\' already exists.')
            return
        elif os.path.isdir('data/'):
            open('data' + os.sep + 'initial.txt', 'x').close()
            print('\'initial.txt\' has been created.')
        else:
            os.mkdir('data/')
            open('data' + os.sep + 'initial.txt', 'x').close()
            print('A new file has been created to: ' +
                  str(os.path.realpath('data' + os.sep + 'initial.txt')))
    except Exception:
        print('An error occured: ' + str(Exception))


def write_file():
    try:
        initial_text_1 = open('data' + os.sep + 'initial.txt', 'w')
        initial_text_1.write(text_to_write)
        initial_text_1.close()
        initial_text_2 = open('data' + os.sep + 'initial.txt', 'r')
        print(str(len(initial_text_2.readlines())) + ' lines has been writen.')
    except Exception:
        print('An error occured: ' + str(Exception))


def change_words():
    try:
        opening_file_text = open('data' + os.sep + 'initial.txt', 'r')
        file_text = opening_file_text.read()
        print(file_text)
        print('Please enter words to replace the ones below:')
        for words in ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]:
            while file_text.find(words) > -1:
                file_text = file_text.replace(words,
                        input("Enter a(n) %s: " % (words.lower())), 1)
        opening_file_text = open('data' + os.sep + 'initial.txt', 'w')
        opening_file_text.write(file_text)
        opening_file_text.close()
        print(file_text)
    except Exception:
        print('An error occured: ' + str(Exception))


if __name__ == '__main__':
    create_dir_and_file()
    write_file()
    change_words()
