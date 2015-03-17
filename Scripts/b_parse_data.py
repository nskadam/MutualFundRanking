# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:15:52 2014

@author: Nilesh
"""
import os
import requests
import datetime
import zipfile
import StringIO
import pandas as pd
import numpy as np

os.chdir('D:\\0. Nilesh Files\\7.1. Personal\\15.4 MF Ranking\\Mutual Fund Ranking\\')

def parse_mf_data():
    time_start = datetime.datetime.now()
    fetched_file_names = os.listdir('Data\\MF Daily\\')
    df_list = list()
    counter =  0
    number_of_files = len(fetched_file_names)
    for file_name in fetched_file_names:
        try:
            # print 'Working on file: ', file_name
            zip_file= zipfile.ZipFile('Data\\MF Daily\\'+file_name, 'r')
            f_name = zip_file.namelist()[0]
            df_temp = pd.read_csv(StringIO.StringIO(zip_file.read(f_name)), sep = ';')
            df_list.append(df_temp)    
        except:
            pass
        counter = counter + 1
        if counter % 50 == 0:
            print 'Time remaining: ', (number_of_files - counter) * \
            (datetime.datetime.now() - time_start) / counter
    df = pd.DataFrame(np.concatenate([df.values for df in df_list]), \
    columns=df_list[0].columns) 
    return df
        
def main():
    df = parse_mf_data()
    df.to_csv('Data\\mf_data_parsed.csv')

if __name__ == '__main__':
    main()    

