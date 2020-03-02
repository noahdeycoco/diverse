# /usr/bin/env python3
# coding:utf_8

import pandas as pd
import xlrd
import os
import shutil
import glob

def prog():
    try:
        excel_files = glob.glob('*.xlsx')
        for y in excel_files:
            
            my_excel_file_path = y
            xls = xlrd.open_workbook(my_excel_file_path, on_demand=True)
            sheet_names = xls.sheet_names()
            
            df = {}
            for i in sheet_names:
                df[i] = pd.read_excel(my_excel_file_path, sheet_name=i)
            
            df.keys()
            df_keys_names = [v for v in df.keys()]
            
            df_names = []
        
            for i in df_keys_names:
                df_names.append(i.replace(".",""))
            
            dir_name = my_excel_file_path.split('.')[0]
            
            # create directory with same file name
            if dir_name in os.listdir('.'):
                shutil.rmtree(dir_name)
                os.mkdir(dir_name)
            else :    
                os.mkdir(dir_name)
            
            for i in df.keys():
                if os.path.exists(os.path.join(dir_name, (dir_name+"_"+i))):
                    os.remove(os.path.join(dir_name, (dir_name+"_"+i+".csv")))
                    #writer = pd.ExcelWriter(os.path.join(dir_name, (dir_name+"_"+i+".xlsx")))
                    #df[i].to_excel(writer, index=False)
                    df[i].to_csv(os.path.join(dir_name, (dir_name+"_"+i+".csv")), encoding='utf-8-sig', index=False)
                    #writer.save()
                else:
                    #writer = pd.ExcelWriter(os.path.join(dir_name, (dir_name+"_"+i+".xlsx")))
                    #df[i].to_excel(writer, index=False)
                    df[i].to_csv(os.path.join(dir_name, (dir_name+"_"+i+".csv")), encoding='utf-8-sig', index=False)
                    #writer.save()
    except Exception as e:
        f = open("LOG - excel_sheets_extractor.txt","w+")
        f.write(str(datetime.datetime.now())+' - ERROR: '+str(e))
        f.close()


if __name__ == '__main__':
    prog()