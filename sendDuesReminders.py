import smtplib
import json
import pandas as pd


# Read data from excel file
df = pd.read_excel('data/duesRecords.xlsx')
print(df)
print('\n --- \n')

df_columns_list_raw = list(df.columns[2:])

# Get people info regarding haven't paid
unpaid_dict = {}
for i in df_columns_list_raw:
  df_unpaid = df[['Member', 'Email', i]][df[i] != 'paid']
  if df_unpaid.empty:
    pass
  else:
    unpaid_dict.update(df_unpaid.to_dict())

# print(unpaid_dict)
# print(unpaid_dict.keys())
# print(list(unpaid_dict['Member'].keys()))
# print(unpaid_dict['Member'][0])


# Log in to an SMTP server by calling smtplib.SMTP(), ehlo(), starttls(),
# and login().
# For all members behind on their dues, send a personalized reminder
# email by calling the sendmail() method.



smtpObj = smtplib.SMTP('smtp.mail.me.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

with open('data/config.json') as json_file:
    config = json.load(json_file)

smtpObj.login(data.get('mail'), data.get('password'))

# msg = ('From: {}\r\nTo: {}\r\n\r\nBonjour {} !'.format(smtpObj.user, smtpObj.user,'Noe'))

# smtpObj.sendmail(from_addr=smtpObj.user, to_addrs=smtpObj.user, msg=msg)

smtpObj.quit()