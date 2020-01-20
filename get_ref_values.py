"""
Multi-lines comments are a demand to alter source code
Single line comments are code explanation
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
from sqlalchemy import create_engine

import json
import pandas as pd
import psycopg2
import time
import sys
import sqlalchemy

with open(r'..\data\default_ref.json') as json_file:
    default_ref = json.load(json_file)

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('token.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))


# Create spreadsheet
"""
Spreadsheet is created at the beginning of the script instead of the end. Thoses lines must be placed at the end
because if an error appear below, we will just have an empty sheet.
"""
# Use the ref_cc for spreadsheet name from the default_ref.json
spreadsheet_body ={
  "properties": {
    "title": str(default_ref['db_table'])+' [%s]' %time.ctime()
  },
  "sheets": [
    {
      "properties": {
        "title": "reference_values"
      }
    }
  ]
}

"""
Add path where Google Spreadsheet must be created
"""
request = service.spreadsheets().create(body=spreadsheet_body)
response = request.execute()
#Catch the spreadsheet id, we'll use it below to write result from prod_
new_spreadsheet_id = response['spreadsheetId']
print('A Google Spread Sheet named \''+spreadsheet_body['properties']['title']+'\' has been created in your personal Google Drive.\n')



# Connection to spreadsheet w/ queries to execute on prod_
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
RANGE_NAME = str(choice_template_spreadsheet)+"_queries_extract_ref_values!A1:F"  #Match the gid (in other words the sheet ID)
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
print('Connection to template spreadsheet established. Spreadsheet available at: https://docs.google.com/spreadsheets/d/'+SPREADSHEET_ID)
values = result.get('values', [])
df = pd.DataFrame.from_dict(values)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df

#Cleaning and formatting: first row values to columns values
columns_names = df.loc[0]
df = df[1:]  #Delete first row; alternative: df.drop(0)
df = df.rename(columns=columns_names)
#df = df.rename(index=str, columns={'valeurs de reference': 'ref_values'})

pd.set_option('display.max_colwidth', -1)

#Delete empty queries
if len(df[df['query'].isnull()]) > 0:
    print ("Reference values below will not be searched because the query is missing:\n")
    print (df[df['query'].isnull()].to_string(index=False))
df = df.mask(df.astype(object).eq('None')).dropna()


#Connection to 192.168.1.120
engine = create_engine('postgresql://'+default_ref['db_user']+':'+default_ref['db_password']+'@192.168.1.120/referentiel')
#Print all differents options for user
query = "select datname from pg_database"
prod_db_list = []
if __name__ == "__main__":
    print ('\nReference values are available on those databases: \n=====')
    data = pd.read_sql(query, engine)
    for i in data.datname:
        if i[0:4] == 'prod':
            print(i)
            prod_db_list.append(i)
    print ('=====')
prod_db = raw_input('Please provide territory where reference values will be fetch. \nExample: for "prod_bretagne_pays_loire", enter "bretagne_pays_loire". ')

#Check if user input is correct: the base name must exist on the server
while (str('prod_'+prod_db)) not in prod_db_list:
    print ('prod_'+prod_db+' not found on '+default_ref['db_host'])
    prod_db = raw_input('Please provide territory where reference values will be fetch. \nExample: for "prod_bretagne_pays_loire", enter "bretagne_pays_loire".')


result = []
#Connection to a prod_'prod_db' in order to execute SQL queries catched above
conn = psycopg2.connect('dbname =prod_'+prod_db+' user='+default_ref['db_user']+' password='+default_ref['db_password']+' host='+default_ref['db_host'])
print ('\nConnection to prod_'+prod_db+' established. Results will be fetch on this database.\n')
cursor = conn.cursor()

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

        ref_values = []

        start_time = time.time()
        #Delete iloc to execute all queries
        for i in df['query'].iloc[0:5]:
            try:
                df_result = pd.read_sql_query(i.encode("utf-8"), conn)
                ref_values.append(df_result.iloc[0][0])
            except Exception:
                ref_values.append("")
        print(str(len(ref_values))+' has been catched: '+str(ref_values))
        print("\nExecuted in: %s seconds" % (time.time() - start_time))
        loading = False
    except Exception as e:
        print("Error: " + str(e))

print(str(len(ref_values)) + " sql results have been extracted from " + str('prod_' + prod_db)+'.')
print("End of extraction.\n")

#Line below add enough elements to create df.ref_values. If this line is executed, check source  for errors
while len(ref_values) <> len(df):
    ref_values.append("")

df["ref_values"] = ref_values
list_tolerance = 0
list_tolerance_p = -1
"""
Tolerances must be copied from the template
"""
df['tolerance'] = list_tolerance
df['tolerance_percent'] = list_tolerance_p
df = df[['result_type', 'validation_type', 'nb', 'name', 'tolerance', 'tolerance_percent', 'ref_values', 'id_requete_extract']]

#Reference values to paste into the first Google SpreadSheet

newlist = [list(df.columns)] + [list(i) for i in list(df.values)]
values = newlist

#df -> newlist -> values -> body; df is transform into a json object in order to be taken in charge by Google
body = {
    'values': values
}

result = service.spreadsheets().values().update(spreadsheetId=new_spreadsheet_id, range="reference_values",valueInputOption='RAW', body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells'))+' References values are available at: https://docs.google.com/spreadsheets/d/'+new_spreadsheet_id+'\n Please copy spreadsheet ID: '+new_spreadsheet_id)