import requests
import time

url = "https://www.kvg-kiel.de/internetservice/services/passageInfo/stopPassages/stop"
data = {
    "language": "de",
    "stop": "2239", # ID of the bus stop
    "mode": "departure",
    "cacheBuster": int(time.time() * 1000), # current timestamp in milliseconds
}
response = requests.post(url, data=data)

if response.status_code == 200:
    arrivals = response.json()
else:
    arrivals = None

for arrival in arrivals['actual']:
    #if arrival['actualRelativeTime'] > 70:
    #    arrivaltime = str(arrival['actualRelativeTime']/60) + " Stunden."
    #else:
    #    arrivaltime = str(arrival['actualRelativeTime']) + " Minuten."
    arrivaltime = str(arrival['actualRelativeTime'] / 100) + " Minuten."
    print("Bus "+arrival['patternText'] + " nach " + arrival['direction'] + " fährt in " + str(round((arrival['actualRelativeTime']/60))) + " Minuten.")


print(arrivals)