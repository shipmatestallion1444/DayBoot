import requests
import time
# Coordinates of Kiel: 54.32133 10.13489
# 54.3217/10.1412
# OpenWeather API key: d056c9342b30b7eb2802231b3f1d2c54

# API GET request URL with Kiel and the API key
url = "https://api.openweathermap.org/data/2.5/weather?lat=54.32&lon=10.13&appid=d056c9342b30b7eb2802231b3f1d2c54"

# Make the request and extract the information
response = requests.get(url)

# Parse it to .JSON
data = response.json()

# Extract the required information
temperature = data["main"]["temp"]
temperature_c = round(temperature - 273.15)
feels_like_temperature = data["main"]["feels_like"]
feels_like_temperature_c = round(feels_like_temperature - 273.15)
rain_status = data["weather"][0]["description"]
rain_outlook = "It will rain soon!" if "rain" in data else "It'll stay dry - hopefully"

# Output the information
print (data)
print(f"{temperature} KELVIN")
print(f"Temperature: {temperature_c} °C")
print(f"Feels Like: {feels_like_temperature_c} °C")
print(f"Rain Status: {rain_status}")
print(f"{rain_outlook}")

