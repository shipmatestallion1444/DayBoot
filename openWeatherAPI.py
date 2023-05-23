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
feels_like_temperature = data["main"]["feels_like"]
rain_status = data["weather"][0]["description"]
rain_soon = "Yes" if "rain" in data else "No"

# Output the information
print(f"Temperature: {temperature} K")
print(f"Feels Like: {feels_like_temperature} K")
print(f"Rain Status: {rain_status}")
print(f"Rain Soon?: {rain_soon}")

