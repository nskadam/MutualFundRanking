# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 22:54:22 2015

@author: Pallavi
"""

import urllib2
import datetime
import os


data_dir = "D:/0. Nilesh Files/7.1. Personal/15.4 MF Ranking/Mutual Fund Ranking"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

files = os.listdir(data_dir + "/Data/NSE Daily/")
current_time =  datetime.date.today()
for i in range(7000):
    year = current_time.strftime("%Y")
    month = current_time.strftime("%b").upper()
    day = current_time.strftime("%d") 
    current_time = current_time - datetime.timedelta(1)
    filename = "cm" + day+month+year+"bhav.csv.zip"
    url = "http://www.nseindia.com/content/historical/EQUITIES/" + year + "/" + month + "/" + filename
    req = urllib2.Request(url,headers = hdr)

    if filename in files:
        continue

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
        
    content = page.read()
    print filename
    output = open(data_dir + "/Data/NSE Daily/" + filename, "wb")
    output.write(content)
    output.close()

