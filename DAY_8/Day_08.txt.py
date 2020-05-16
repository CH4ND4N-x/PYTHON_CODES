# Data Exchange Mechanism 
# Javascript Object Notation (JSON)
"""
Python          JSON
dict            object  { }           Useful to store info for single object
list            array   [  ]          Useful to store infor for multiple
str             string  "  "          
int             number  89, 98.67
True            true    true
False           false   false 
None            null    null
"""

# Loading raw json data into python specific data 
import json

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
print (type(json_string))

# Converts  JSON Data types to Python Data Types 
my_data = json.loads(json_string)

print (type(my_data) )  # its a python dictionary
print (my_data) 
print (my_data['researcher'])
print (my_data['researcher']['relatives'])
print (my_data['researcher']['relatives'][0])
print (my_data['researcher']['relatives'][0]['name'])



"""
( URL  --> HTML Page )               Website
( URL  --> JSON / XML /RAW TEXT )    API

Introduce to the concept of Web Services ( REST API ) using openweathermap.org

1. Sign Up
2. API Doc 
3. get API URL 

http://www.openweathermap.org
  

http://api.openweathermap.org/data/2.5/weather?q=Jaipur

http://api.openweathermap.org/data/2.5/weather?q=Jaipur&appid=e9185b28e9969fb7a300801eb026de9c


# if you hit the URL in the browser and try to visualise the JSON, 
# you will come to see that it has 12 items in the object 
# copy and paste this on jsonlint.com and visualise 

# What is the ROOT DataType

# coord as Object
    {
     #   lon as Number
     #   lat as Number
    }
# weather as List
    [ 
     {
         #  id as Number
         #  main as String
         #  description as String
         #  icon as String
     }
     ]
# base as String
# main as Object 
    {
        # temp as Number
        # pressure as Number
        # humidity as Number
        # temp_min as Number
        # temp_max as Number
    }
# visibility as Number
# wind as Object
    {
        # speed as Number
        # deg as Number
    }
# clouds as Object
    {
     # all as Number
    }
# dt as Number
# sys as Object
    # type as Number 
    # id as Number
    # message as Number
    # country as String
    # sunrise as Number
    # sunset as Number
# id as Integer
# name as String
# cod as Number
"""



# Get me the temperature of the city from the openweathermap.org using request library


import requests


city = input("Enter city name: ")


url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=" + city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
jsondata = response.json()
print (jsondata['main']['temp'])



# Reading the JSON Data
print (jsondata)
print (type(jsondata))
print (jsondata.keys())
print (jsondata.values())
print (len(jsondata.items()))
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")




# Converting EPOCH time to HUMAN readable time
# The Unix epoch is the time 00:00:00 on 1 January 1970.
    
import time
time.ctime(jsondata["sys"]["sunrise"])
    

import datetime
datetime.fromtimestamp(jsondata["sys"]["sunset"])    
