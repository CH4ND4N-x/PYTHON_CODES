#Webscrapping ICC Cricket Page
from bs4 import BeautifulSoup
import requests
import pandas as pd
URL="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

source_code=requests.get(URL).text
soup = BeautifulSoup(source_code,"lxml")

right_table=soup.find('table',class_='table')
"""
1st tr =5th
2nd tr =5td
3rd tr =5td
.
.
.
21st tr=5td
"""
final_data={'TEAM':[],
            'MATCHES':[],
            'POINTS':[],
            'RATING':[]
            }
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells)==5:
        final_data['TEAM'].append(cells[1].text.strip()[:-4:])
        final_data['MATCHES'].append(cells[2].text.strip())
        final_data['POINTS'].append(cells[3].text.strip())
        final_data['RATING'].append(cells[4].text.strip())
"""
to save it as csv use below line of code
(pd.DataFrame.from_dict(data=final_data, orient='index').to_csv('icccricket.csv', header=False))       
"""
#printing the final data
show_data = pd.DataFrame(final_data)
print(show_data)