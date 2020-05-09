# quickWeather.py - Prints the weather for a location from the command line.
import json
import requests

#, sys
# Compute location from command line arguments.
apiKey = '0c35fbc4cde0783c9ab435bf051583c0'

# exclude vars params:
# current
# minutely
# hourly
# daily

# https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.44&appid=0c35fbc4cde0783c9ab435bf051583c0

# if len(sys.argv) < 2:
#   print('Usage: quickWeather.py location')
#   sys.exit()

# 

# TODO: Download the JSON data from OpenWeatherMap.org's API.
lat = '33.44'
lon = '-94.44'
exclude = 'minutely,hourly,daily'
city_name = 'Middleberg'
# apiURL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}'.format(lat, lon, exclude, apiKey)
apiURL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, apiKey)
res = requests.get(apiURL)

# TODO: Load JSON data into a Python variable.
jsonResult = json.loads(res.text)

data = dict(jsonResult)

print(data.keys())

print(data['main'])
print(data['weather'][0]['description'])
print(data['weather'])
