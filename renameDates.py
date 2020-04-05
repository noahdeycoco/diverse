import os
# import regex
import datetime
import random
import re

"""
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to Europeanstyle dates
(DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
"""

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2020, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

directory = "data"+os.sep+"dates"


def write_date_files(): 
    for i in range(0,10):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        file_name = str(random_date)+".txt"

        open(directory+os.sep+file_name, 'a').close()
        print(file_name + ' has been written to ' + directory  + ".")


def change_datetime():
    files_to_rename = []
    for i in os.listdir(directory):
        date_file = i.split(sep='.txt')[0]
        try:
            datetime.datetime.strptime(date_file, '%Y-%m-%d')
            files_to_rename.append(i)
        except ValueError:
            raise ValueError("Incorrect data format for %s, should "
                             "be YYYY-MM-DD" % (date_text))

    for i in files_to_rename:
        new_file = datetime.datetime.strptime(date_file, '%Y-%m-%d').strftime('%d-%m-%Y')+".txt"
        os.rename(directory+os.sep+i, new_file)
        print(str(i) + ' has been renamed to ' + new_file + ".")

def delete_files():
    delete_files = []
    for i in os.listdir(directory):
        delete_files.append(i)
        os.remove(directory+os.sep+i)
    print("File(s) delete in " + str(directory) + str(delete_files))
    print("ls " + str(directory) + " >>> " + str(os.listdir(directory)))


if __name__ == "__main__":
    try:
        pass
        write_date_files()
        # change_datetime()
        delete_files()
    except Exception as e:
        print(e)
