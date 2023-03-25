import requests
import json


city = "Grand Prairie"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
Api_key = '47a2290beeb0bd6655c0621fd2c15f15'
url = base_url + "appid=" + Api_key + "&q=" + city

response = requests.get(url)
data = response.json()
if data["cod"] != "404":

        y = data["main"]
        temp = y["temp"]
        temp = temp - 273.15
        temp = (temp * 9/5) + 32 
        temp = int(temp)
        print(f"Temputare: {temp}°F")
