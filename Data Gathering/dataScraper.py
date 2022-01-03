import sys, os, time
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer

'''
Could use urllib2, I thought it would be more complicated so started with selenium
'''
chromedriver_path = 'C:\Webdrivers\chromedriver.exe'
link = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

browser = webdriver.Chrome(chromedriver_path,options=options)
browser.get(link)#open website
print('waiting...')
time.sleep(5)
print('waiting over')
browser.find_element_by_class_name('css-47sehv').click()#accept cookies (site requires javascript)
time.sleep(5)
html = browser.page_source#load html from page
soup = bs(html)#load html in beautiful soup
table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="stats_standard")
rows = table.findAll(lambda tag: tag.name=='tr')
print(len(rows))

dfs = pd.read_html(html)
print(dfs)
print(dfs[-1])
dfs[-1].to_csv('Player Stats 21-22.csv')
