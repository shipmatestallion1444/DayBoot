import requests
import time

def get_bus_schedule():
    url = "https://www.kvg-kiel.de/internetservice/services/passageInfo/stopPassages/stop"
    data = {
        "language": "de",
        "stop": "2239",  # ID of the bus stop, 2239 being Südfriedhof
        "mode": "departure",
        "cacheBuster": int(time.time() * 1000),  # current timestamp in milliseconds
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:  # request is successful
        arrivals = response.json()['actual']
        schedule = [{'ankunft': round(arrival['actualRelativeTime'] / 60),
                     'buslinie': arrival['patternText'],
                     'richtung': arrival['direction']} for arrival in arrivals]
        return schedule
    else:  # request is unsuccessful
        return None