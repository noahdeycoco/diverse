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

def main():

    with open(r'..\data\default_ref.json') as json_file:
        default_ref = json.load(json_file)

    try:
        conn = psycopg2.connect("dbname ="+default_ref['db_schema']+" user="+default_ref['db_user']+" password="+default_ref['db_password']+" host="+default_ref['db_host'])
        cursor = conn.cursor()
        cursor.execute('SELECT sql_file_name, result FROM '+default_ref['db_schema']+'.'+default_ref['db_table'])
        data = cursor.fetchall()
    except Exception as e:
        print("Error: " + str(e))


    ref_list =[]
    for row in data:
        ref_list.append(row)
    df_db_ref = pd.DataFrame.from_records(ref_list, columns=['indic_name', 'result'])

    indic_liste = []
    for i in df_db_ref.indic_name.str.split('_', n=2):
        a = i[2:]
        b = ''.join(a) #Transform list into string to avoid [] for each elements during list creation below
        indic_liste.append(b)

    #Felete indic_name id
    df_db_ref = df_db_ref.assign(name_wo_id = indic_liste)
    df_db_ref.head()

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
    #Call the sheets API
    """
    A list recaps the differents templates for each model. It is hardcoded as you can see below, and must be changed.
    Program needs to read through an API features all templates on google (SCOPE must be changed btw) and print which template exists.
    """
    template_spreadsheet = {
    "dynex": "",
    "ewan": "",
    "experts": "",
    "mcm": "",
    "next": "",
    "ppg": "",
    "scolator": "",
    "strass": "",
    "ttt":  "",
    "wasci": "",
    "wasp": ""
    }

    print ('Available templates models:\n=====')
    for i in template_spreadsheet:
        print(i)
    print ('=====')

    choice_template_spreadsheet = raw_input('Please enter the model where reference values will be fetch.')
    while choice_template_spreadsheet not in template_spreadsheet:
        print (str(choice_template_spreadsheet)+' not found in the list above.')
        choice_template_spreadsheet = raw_input('Please enter the model where reference values will be fetch.')

    model_template_spreadsheet = template_spreadsheet[choice_template_spreadsheet]
    print(choice_template_spreadsheet)
    SPREADSHEET_ID = model_template_spreadsheet  #ID in google spreadsheet url
    RANGE_NAME = str(choice_template_spreadsheet)+'_template_ref_values' #Match the gid (in other words the sheet ID)
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    df_gg_ref = pd.DataFrame.from_dict(values)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df_gg_ref


    #Cleaning and formatting
    columns_names = df_gg_ref.loc[0]
    df_gg_ref = df_gg_ref[1:]  #Delete first row; alternative: df.drop(0)
    df_gg_ref = df_gg_ref.rename(columns=columns_names)
    #df = df.rename(index=str, columns={'valeurs de reference': 'ref_values'})
    df_gg_ref = df_gg_ref.drop(columns=['result_type', 'validation_type', 'nb', 'tolerance', 'tolerance_percent'])

    #Delete '.sql' @ the end of 'indic_name'
    df_gg_ref = df_gg_ref.assign(new_name = df_gg_ref.name.str[:-4])
    df_gg_ref = df_gg_ref.drop(columns='name')
    df_gg_ref = df_gg_ref.rename(columns={'new_name': 'name'})
    df_gg_ref = df_gg_ref[['name', 'ref_values']]

    #Get dataframe where ref_values must be superior to 0
    df_new_gg_ref = df_gg_ref[(df_gg_ref.ref_values == '> 0') | (df_gg_ref.ref_values == '>0')]

    df_with_errors = df_db_ref[df_db_ref.name_wo_id.isin(df_new_gg_ref.name)]
    #Indic_name with result equal to 0 are errors
    if len(df_with_errors) > 0:
        print (str(len(df_with_errors))+' row(s) in '+str(default_ref['db_schema']) + '.' + str(default_ref['db_table'])+' have a \'result\' superior to 0. Have a look:')
        print(df_with_errors[df_with_errors.result == 0][['indic_name', 'result']])
        print ('\nConsult template rules at: https://docs.google.com/spreadsheets/'+SPREADSHEET_ID+'/ .')
    else:
        print ('All data in '+str(default_ref['db_schema']) + '.' + str(default_ref['db_table'])+' seems to respect template rules available at: https://docs.google.com/spreadsheets/'+SPREADSHEET_ID+'/ . ')


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