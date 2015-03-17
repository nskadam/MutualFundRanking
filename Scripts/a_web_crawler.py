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
import pandas.io.data

os.chdir('D:\\0. Nilesh Files\\7.1. Personal\\15.4 MF Ranking\\Mutual Fund Ranking\\')

class Job:
    def add_job(self, domain_url):
        pass
    def get_all_jobs(self):
        pass
    

class WebCrawler:
    pass

class Crawler:
    def get_data(url):
        pass


def get_daily_mf_data():
    date = datetime.datetime.now().date()
    fetched_file_names = os.listdir('Data\\\\MF Daily\\\\')
    fetched_file_names_san  = [ os.path.splitext(fl)[0] for fl in fetched_file_names]
    for i in xrange(3000):
        date = date + datetime.timedelta(days = -1)
        # print 'Checking if data is fetched for date: ', date
        file_name_san = 'mf_data_date_' + str(date)
        if file_name_san not in fetched_file_names_san:
            try:
                print 'Fetching for date: ', date
                date_string = date.strftime('%d-%b-%Y')
                # url = 'http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=03-Nov-2014&todt=03-Nov-2014'
                url = 'http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt='+date_string+'&todt='+date_string
                req = requests.get(url)
                zf = zipfile.ZipFile('Data\\\\MF Daily\\\\' + file_name_san + '.zip', mode='w', 
                                     compression=zipfile.ZIP_DEFLATED)
                zf.writestr(file_name_san + '.txt', req.text.encode('UTF-8'))
                zf.close()
            except:
                pass

def get_index_data():
    start_date = datetime.datetime.strptime('1991-01-01','%Y-%m-%d')
    end_date = datetime.datetime.now()
    start_date.date()
    f=pandas.io.data.DataReader("^NSEI", 'yahoo', start_date, end_date)
    f.to_csv('Data\\Index\\nifty.csv')
    
def main():
    get_daily_mf_data()
    get_index_data()

if __name__ == '__main__':
    main()    

