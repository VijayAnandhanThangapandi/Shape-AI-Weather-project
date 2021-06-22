import requests
#import os
from datetime import datetime

api_key = '1fa35c68cf1068a8a426aa16095e65a8'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

output = "-------------------------------------------------------------\n"
output += "Weather Stats for - {} || {}\n".format(location.upper(), date_time)
output += "-------------------------------------------------------------\n"
output += "Current temperature is: {:.2f} deg C\n".format(temp_city)
output += f"Current weather desc :{weather_desc}\n"
output += f"Current Humidity :{hmdt}% \n"
output += f"Current wind speed :{wind_spd}kmph \n"

f=open("output.txt", "a")
f.write(output)
f.close()