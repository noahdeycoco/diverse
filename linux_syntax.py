#!/usr/bin python2.7
#-*- coding: utf-8 -*-
import os
import time

# Le script doit être placé dans le dossier dans lequel la syntaxe des fichiers
# et dossiers doivent être modifiés.
main_path = os.path.dirname(os.path.abspath(__file__))

def folder_to_edit():
    print("==========\nThe current script will run on '"+ main_path
          +"'.\n==========")

def syntaxing():

    # On instance plusieurs variables afin de donner du contrôle à l'utilisateur
    edit_check = 0
    check_dir_to_edit = 0
    check_files_to_edit = 0
    edit_count = 0

    for root, dirs, files in os.walk(main_path, topdown=False):
        for name in dirs:
            all_dir = os.path.join(root, name)
            all_dir_new = os.path.join(root, name.replace(' - ', '_').replace(' ',
                                '_').replace('-', '_').replace('é', 'e').lower())
            if all_dir != all_dir_new:
                while check_dir_to_edit < 1:
                    print("\nDirectories below will be edited : \n")
                    check_dir_to_edit=2
                print(all_dir + " ==> " + all_dir_new)
                edit_check += 1

    for root, dirs, files in os.walk(main_path, topdown=False):
        for name in files:
            all_files = os.path.join(root, name)
            all_files_new = os.path.join(root, name.replace('_-_','_').replace(' - ', '_').replace(' ',
             '_').replace('-', '_').replace('é', 'e').lower())
            if all_files != all_files_new:
                while check_files_to_edit < 1:
                    print ("\nFiles below will be edited : \n")
                    check_files_to_edit = 2
                print(all_files + " ==> " + all_files_new)
                edit_check += 1

    if edit_check == 0:
        print("\nSyntaxing is correct.\nProgramm exit.")
        exit()
    else:
        response = str(input("\nContinue (y/n) "
                                 ":"))
        wainting_user_response =0
        while wainting_user_response < 1:
            if response == "y" or response == 'Y':
                start_time = time.time()
                for root, dirs, files in os.walk(main_path, topdown=False):
                    for name in dirs:
                        all_dir = os.path.join(root, name)
                        all_dir_new = os.path.join(root,
                                                   name.replace('_-_','_').replace(' - ', '_').replace(' ',
                                    '_').replace('-', '_').replace('é', 'e').lower())
                        if all_dir != all_dir_new:
                            os.rename(all_dir, all_dir_new)
                            edit_count += 1
                    for name in files:
                        all_files = os.path.join(root, name)
                        all_files_new = os.path.join(root, name.replace('_-_','_').replace(' - ',
                                                                        '_').replace(' ',
                                         '_').replace('-', '_').replace('é', 'e').lower())
                        if all_files != all_files_new:
                            os.rename(all_files, all_files_new)
                            edit_count += 1

                print(
                    str(edit_count) + " files or directories has "
                                                            "been edited  with linux "
                                                            "syntaxing.")

                print("--- Executed in %s seconds ---\n Programm exit." % (time.time() -
                                                                           start_time))
                wainting_user_response += 1

            elif response == 'n' or response == 'N':
                print('Programm exit')
                exit()

            elif response is None or response not in ['Y', 'y', 'N', 'n']  :
                response = str(input("Please enter a valid option choice ("
                                     "y/n) :"))
            else:
                print('Programm exit')
                exit()


if __name__ == "__main__":
    folder_to_edit()
    syntaxing()
