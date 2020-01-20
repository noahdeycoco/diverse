# coding: utf-8
# !/usr/bin/env python
"""
Multi-lines comments are a demand to alter source code
Single line comments are code explanation
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import json
import pandas as pd
import psycopg2
import time
import sys


def sleep(self):
    self.sleep()

def main():
    with open(r'..\data\default_ref.json') as json_file:
        default_ref = json.load(json_file)

    #Get ref data
    #Setup the sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json',
                                              SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    SPREADSHEET_ID = str(raw_input('Please provide Google Spreadsheet ID.\nThe spreadsheet may be present in your personnal Google Drive.\n\nEvery API method requires a spreadsheetId parameter which is used to identify which spreadsheet is to be accessed or altered. This ID is the value between the "/d/" and the "/edit" in the URL of your spreadsheet. For example, consider the following URL that references a Google Sheets spreadsheet: docs.google.com/spreadsheets/d/1qpyC0XzvTcKT6EISywvqESX3A0MwQoFDE8p-Bll4hps/edit#gid=0. The ID of this spreadsheet is 1qpyC0XzvTcKT6EISywvqESX3A0MwQoFDE8p-Bll4hps.')) #ID in google spreadsheet url
    RANGE_NAME = 'reference_values!A1:G'  #Match the gid (in other words the sheet ID)
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    df = pd.DataFrame.from_dict(values)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df

    #Cleaning and formatting: first row values to columns values
    columns_names = df.loc[0]
    df = df[1:]  #Delete first row; alternative: df.drop(0)
    df = df.rename(columns=columns_names)
    #df = df.rename(index=str, columns={'valeurs de reference': 'ref_values'})
    df = df.drop(columns=['result_type', 'validation_type', 'nb'])

    #Check 'NaN' in 3 columns
    df_tol_null = df[df.tolerance.isnull()]
    df_tol_p_null = df[df.tolerance_percent.isnull()]
    df_ref_null = df[df.ref_values.isnull()]

    #Check digit in 3 columns
    df_tol_digit = df[df['tolerance'].str.encode('utf-8', errors='ignore').str.isdigit().fillna(
        False)]  # fillna(False) delete rows where ref_values <> digit
    """
    tol_p est constitué de -1 et autres numeros, isdigit() prend en considération '-' et doit être utilisé autrement
    pour verifier que tol_p ne comporte que des nums 
    df_tol_p_digit = df[df['tolerance_percent'].str.encode('utf-8', errors='ignore').str.isdigit().fillna(False)]
    ---
    SOLUTION: try with pd.to_numeric(df['a']).dropna()
    """
    df_ref_digit = df[df['ref_values'].str.encode('utf-8', errors='ignore').str.isdigit().fillna(False)]

    #Dataframes designing with errors
    df_check_tol_digit = df.loc[df.tolerance.isin(df_tol_digit.tolerance) == False]
    df_check_ref_digit = df.loc[df.ref_values.isin(df_ref_digit.ref_values) == False]

    #Concat all dataframes into one with every errors
    frames = [df_tol_null, df_tol_p_null, df_ref_null, df_check_tol_digit, df_check_ref_digit]
    df_incorrect_ref = pd.concat(frames)

    #Dataframe to insert in base
    """
    from here, script must be modified by using df.to_sql() in order to catch errors
    warning: create a class to prevent SQL execution beginning with anything else that UPDATE 
    """
    reference = df.loc[df.ref_values.isin(df_incorrect_ref.ref_values) == False]

    #dataframe with wrong values: 'df_incorrect_ref'
    print ("\nThe values below will not be taken in the writing process because of bad formatting \n")
    time.sleep(1/2)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print (df_incorrect_ref)
    time.sleep(1/2)
    continuing_choice = raw_input('\nDo you want to continue ? (y/n) \nIf \'yes\', process will operate on '+default_ref['db_schema']+'.'+default_ref['db_table'])

    while continuing_choice == 'y' or continuing_choice == 'Y' or continuing_choice == 'yes':
        try:
            reference = reference.assign(new_name = reference.name.str[:-4])
            reference = reference.drop(columns='name')
            reference = reference.rename(columns={'new_name': 'name'})
            reference = reference[['name', 'tolerance', 'tolerance_percent', 'ref_values']]

            name = reference.name.tolist()
            tolerance = reference.tolerance.tolist()
            tolerance_percent = reference.tolerance_percent.tolist()
            ref_values = reference.ref_values.tolist()

            # Login to access server
            print (('Fetch db_user to access '+str(default_ref['db_host'])+'.'+str(default_ref['db_port'])+' \n ****'))
            user_name_bd = default_ref['db_user']
            """"
            enjoy yourself to replace the stars by the exact number of characters for id and password
            """
            print (('Fetch db_password \n ****'))
            password_bd = default_ref['db_password']

            check_value = raw_input("Do you want to see which values will be changed? (y/n)")

            while check_value == 'y' or check_value == 'Y':
                try:
                    print (reference)
                    check_value = 'n'
                except Exception as e:
                    print("Error : " + str(e))
            time.sleep(1)
            print ("Beginning of the writing in reference base\n")
            time.sleep(1)

            loading = True
            loading_speed = 4
            loading_string = "." * 6

            while loading:
                try:
                    for index, char in enumerate(loading_string):
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(2.0 / loading_speed)
                    index += 1
                    sys.stdout.write("\b" * index + "" * index + "\b" * index)

                    conn = psycopg2.connect(
                        "dbname = referentiel user=" + user_name_bd + " password=" + password_bd + " host= 192.168.1.120")
                    cursor = conn.cursor()
                    start_time = time.time()
                    for i, j, o, k in zip(name, tolerance, tolerance_percent, ref_values):
                        cursor.execute("UPDATE referentiel."+default_ref['db_table']+" SET result=" +str(k)+ ", tolerance=" +str(j)+ ", tolerance_percent=" +str(o)+ " WHERE sql_file_name like '%" +str(i)+ "%';")
                        print ("UPDATE referentiel."+default_ref['db_table']+" SET result=" +str(k)+ ", tolerance=" +str(j)+ ", tolerance_percent=" +str(o)+ " WHERE sql_file_name like '%" +str(i)+ "%';")
                    conn.commit()
                    print("\n Executed in: %s seconds" % (time.time() - start_time))
                    loading = False
                except Exception as e:
                    print("Error: " + str(e))

                print(str(len(name)) + " sql queries have been sent to "+str(default_ref['db_schema'])+"."+str(default_ref['db_table']))
                print ("End of writing")

                continuing_choice = 'n'  #Block while loop


        except Exception as e:
            print ("Error : " + str(e))


choice_input = 1

while choice_input == 1:
    try:
        main()
        choice_input = int(input("Type 0 if you want to exit the program or 1 to continue"))

    except Exception as e:
        print("Error : " + str(e))

    except:
        print ("End of program")
        break