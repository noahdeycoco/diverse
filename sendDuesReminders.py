import pandas as pd

df = pd.read_excel('data/duesRecords.xlsx')
print(df)
print('\n --- \n')

df_jan14 = df.iloc[:, [0,1,2]]
# print(df_jan14)

# print(df_jan14.iloc[:, 2])

# print(list(df.columns[2:]))


df_columns_list_raw = list(df.columns[2:])

df_columns_list =  []
for i in df_columns_list_raw:
  df_columns_list.append(i.replace(" ","_").lower())

unpaid_dict = {}
for i in df_columns_list_raw:
  df_unpaid = df[['Member', 'Email', i]][df[i] != 'paid']
  if df_unpaid.empty:
    pass
  else:
    unpaid_dict.update(df_unpaid.to_dict())

# print(unpaid_dict)
