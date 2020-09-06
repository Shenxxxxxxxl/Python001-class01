import os
import schedule
from scrapy import cmdline

def job():
    d = os.path.dirname(__file__)
    abspath = os.path.abspath(d)
    print(abspath)
    scrapy_path = abspath+'/shopping'
    os.system('cd %s && scrapy crawl smzdm '% (scrapy_path) )
    os.system(r'python %s/DataCleaning/data_clean.py'% (abspath))  
schedule.every().day.at('02:00').do(job)