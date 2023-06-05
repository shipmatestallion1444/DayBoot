from flask import Flask, render_template
from lxml import etree
import requests
import feedparser
from api import bus, weather, cinema, localnews, train, calendar

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    bus_schedule = bus.get_bus_schedule()
    weather_data = weather.get_weather()
    NewsFeed = feedparser.parse("https://www.ndr.de/nachrichten/schleswig-holstein/index-rss.xml")
    entries = NewsFeed.entries[:3]  # Get the first 3 news entries
    news_data = [{"title": entry.title,
                  "description": entry.description,
                  "image": entry['mp:image']['mp:data'] if 'mp:image' in entry and 'mp:data' in entry['mp:image'] else None}
                 for entry in entries]

#     cinema_data = cinema.get_cinema_data()
#     localnews_data = localnews.get_news_data()
#     train_schedule = train.get_train_schedule()
#     calendar_data = calendar.get_calendar_data()

    # process data as needed

    return render_template('dashboard.html',
                           bus_schedule=bus_schedule,
                           weather_data=weather_data,
                           news_data=news_data,
                           # cinema_data=cinema_data,
                           # localnews_data=localnews_data,
                           # train_schedule=train_schedule,
                           # calendar_data=calendar_data
                           )

if __name__ == '__main__':
    app.run(debug=True)
