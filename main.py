from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
import time
# from requests_html import HTMLSession



# session=HTMLSession()



driver=webdriver.Chrome()
driver.get('https://hprera.nic.in/PublicDashboard')
# response.html.render()
time.sleep(20)
response=driver.page_source

soup=BeautifulSoup(response,features='html.parser')

# links=soup.find_all('div',class_='tab-pane fade show active')
# new=BeautifulSoup()
for item in soup.findAll('div',attrs={'class':"shadow py-3 px-3 font-sm radius-3 mb-2"}):
    for div in item.findAll('div',attrs={'class':''}):
        for a in div.findAll('a',attrs={'title':'View Application'}):
            print(a.text)

            
        
   
       
           






