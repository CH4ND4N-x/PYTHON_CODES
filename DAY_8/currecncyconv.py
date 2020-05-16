#Currency Converter Convert  from USD to INR
import requests
USD=int(input("Enter USD ->"))
responce=requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=6ef8fae478aa3f89299e")
Current_rate=responce.json()
print("INR ->",USD*Current_rate['USD_INR'])