import requests
import time
# Coordinates of Kiel: 54.32133 10.13489
# OpenWeather API key: d056c9342b30b7eb2802231b3f1d2c54

# API GET request URL with Kiel and the API key
url = "https://api.openweathermap.org/data/2.5/weather?lat=54.32&lon=10.13&appid=d056c9342b30b7eb2802231b3f1d2c54"

# Make the request and extract the information
response = requests.get(url)

# Parse it to .JSON
data = response.json()

# Extract the required information
temperature = data["main"]["temp"]
temperaturec = (temperature - 30)/2
feels_like_temperature = data["main"]["feels_like"]
feels_like_temperature_c = (feels_like_temperature - 30)/2
rain_status = data["weather"][0]["description"]
rain_soon = "It will rain soon!" if "rain" in data else "It'll stay dry - hopefully"

# Output the information
print(f"Temperature: {temperaturec} C")
print(f"Feels Like: {feels_like_temperature_c} C")
print(f"Rain Status: {rain_status}")
print(f"{rain_soon}")

