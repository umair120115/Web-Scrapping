from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('https://hprera.nic.in/PublicDashboard')
# html=driver.page_source
time.sleep(20)
# print(response)
soup=BeautifulSoup(driver.page_source,features='html.parser')
# links=soup.find_all('div',class_='tab-pane fade show active')


for item in soup.findAll('div',class_="shadow py-3 px-3 font-sm radius-3 mb-2"):
    for a in item.findAll('a',attrs={'title':'View Application'}):
        for href in a:
            (a.get('href'))
            



