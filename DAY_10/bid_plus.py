#Bid Plus
#C:\Users\CHANDAN\geckodriver.exe
from  selenium import webdriver
from time import sleep
import requests
import pandas as pd
URL="https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Firefox(executable_path="/Users/CHANDAN/geckodriver.exe")
browser.get(URL)
right_table=browser.find_element_by_id('pagi_content')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for row in right_table.find_elements_by_class_name('add-height'):
    D.append(row.text.rstrip('\n'))
    
    
""""""""""""""""""""
for row in right_table.find_elements_by_class_name('block_header'):
   cells=row.find_elements_by_tag_name('a')
   A.append(cells[0].text.strip())

""""""""""""""""""""
data1=[]
data2=[]
for row2 in right_table.find_elements_by_class_name('col-block'):
    cells2=row2.find_elements_by_tag_name('span')
    if len(cells2)==2:
        data1.append(cells2[0].text.strip())
        data2.append(cells2[1].text.strip())
B=[item for item in data1[::2]]        
E=[item for item in data1[1::2]]   
C=[item for item in data2[::2]]
F=[item for item in data2[1::2]] 

import pandas as pd
df = pd.DataFrame()
df["BID NO"]=A
df["ITEM"]=B
df["QUANTITY"]=C
df["Department Name And Address"]=D
df["Start Date/Time"]=E
df["End Date/Time"]=F

df.to_csv("former.csv")

browser.quit()