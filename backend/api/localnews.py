import feedparser
import requests
def get_news_data():
    response = requests.get("https://www.ndr.de/nachrichten/schleswig-holstein/index-rss.xml")
    if response.status_code == 200:
        NewsFeed = feedparser.parse("https://www.ndr.de/nachrichten/schleswig-holstein/index-rss.xml")
        entries = NewsFeed.entries[:3]  # Get the first 3 news entries
        localnews_data = [{"title": entry.title,
                    "description": entry.description,
                    "image": entry['mp:image']['mp:data'] if 'mp:image' in entry and 'mp:data' in entry[
                        'mp:image'] else None}
                    for entry in entries]
        return localnews_data
    else:
        return None