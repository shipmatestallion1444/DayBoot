from flask import Flask, render_template
from lxml import etree
import requests
import feedparser
from api import bus, weather, nina, cinema, localnews, train, calendar

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    bus_schedule = bus.get_bus_schedule()
    weather_data = weather.get_weather()
    localnews_data = localnews.get_news_data()
    nina_data = nina.get_nina_warnings()

#     train_schedule = train.get_train_schedule()
#     calendar_data = calendar.get_calendar_data()
    # process data as needed

    return render_template('dashboard.html',
                           bus_schedule=bus_schedule,
                           weather_data=weather_data,
                           localnews_data=localnews_data,
                           nina_data=nina_data,
                           # cinema_data=cinema_data,
                           # localnews_data=localnews_data,
                           # train_schedule=train_schedule,
                           # calendar_data=calendar_data
                           )

if __name__ == '__main__':
    app.run(debug=True)
