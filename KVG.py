import requests
import time

url = "https://www.kvg-kiel.de/internetservice/services/passageInfo/stopPassages/stop"
data = {
    "language": "de",
    "stop": "2239", # replace with your stop number
    "mode": "departure",
    "cacheBuster": int(time.time() * 1000), # current timestamp in milliseconds
}
response = requests.post(url, data=data)

if response.status_code == 200:
    arrivals = response.json()
else:
    arrivals = None

for arrival in arrivals['actual']:
    print("Bus "+arrival['patternText'] + " nach " + arrival['direction'] + " fährt in " + str(arrival['actualRelativeTime']) + " Minuten.")

print(arrivals)