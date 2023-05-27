from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

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
        return response.json()
    else:  # request is unsuccessful
        return None


# for arrival in arrivals['actual']:
#
#     ankunft = round(arrival['actualRelativeTime']/60)
#     buslinie = arrival['patternText']
#     richtung = arrival['direction']
#
#     print("Bus "+ buslinie + " nach " + richtung + " fährt in " + str(ankunft) + " Minuten.")
#
#
# print(arrivals)

@app.route('/dashboard')
def dashboard():
    arrivals = get_bus_schedule()
    if arrivals is not None:
        schedule = []
        for arrival in arrivals['actual']:
            ankunft = round(arrival['actualRelativeTime'] / 60)
            buslinie = arrival['patternText']
            richtung = arrival['direction']
            schedule.append({'ankunft': ankunft, 'buslinie': buslinie, 'richtung': richtung})
    else:
        schedule = []
    return render_template('dashboard.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
