import os
# import regex
import datetime
import random

"""
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to Europeanstyle dates (DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
"""

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2020, 1, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

print(random_date)
print(type(random_date))

# for i in range(0,10):

directory = "data"+os.sep+"dates"
print(directory)
# print(os.path.abspath("data"+os.sep+"dates"))
# open(os.path.abspath(directory+os.sep+(str(random_date)+'.txt')),'a' ).close()
