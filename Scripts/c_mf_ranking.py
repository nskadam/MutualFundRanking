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

os.chdir('D:\\0. Nilesh Files\\7.1. Personal\\15.4 MF Ranking\\Mutual Fund Ranking\\')

def main():
    df = pd.read_csv('data/mf_data.csv')
    df
    
if __name__ == '__main__':
    main()    

