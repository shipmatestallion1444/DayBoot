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

    ankunft = round(arrival['actualRelativeTime']/60)
    buslinie = arrival['patternText']
    richtung = arrival['direction']

    print("Bus "+ buslinie + " nach " + richtung + " fährt in " + str(ankunft) + " Minuten.")


print(arrivals)