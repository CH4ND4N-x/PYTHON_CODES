#JSON Parser
#http://www.openweathermap.org
#http://api.openweathermap.org/data/2.5/weather?q=London&APPID=15039720b867f8e232aa8692217b76eb
import time
import requests
city=input("Enter the city->")
URL1="http://api.openweathermap.org/data/2.5/weather?q="
URL2="&APPID=15039720b867f8e232aa8692217b76eb"

URL=URL1+city+URL2
#print(URL)
response = requests.get(URL)
city_data = response.json()

print("Coordinates  ->",city_data['coord'])
print("weather      ->",city_data['weather'][0]['description'])
print("\nWinds      ->",city_data['wind'])
print("\nSunrise at ->",time.ctime(city_data['sys']['sunrise']),
      "\nSunset at  ->",time.ctime(city_data['sys']['sunset']))