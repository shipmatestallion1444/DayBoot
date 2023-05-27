# # https://www.studio-filmtheater.de/#calendar
#
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from time import sleep
#
# # Path to chromedriver.exe
# path_to_chromedriver = 'F:\Programme\chromedriver\chromedriver.exe'
#
# # Initiate a webdriver
# browser = webdriver.Chrome(executable_path=path_to_chromedriver)
#
# # URL of the page
# url = 'https://www.studio-filmtheater.de/#calendar'
#
# # Get the webpage
# browser.get(url)
#
# # Let the browser load the page
# sleep(5)
#
# # Parse the HTML page with Beautiful Soup
# soup = BeautifulSoup(browser.page_source, 'html.parser')
#
# # Close the browser
# browser.quit()
#
# # Now you can use Beautiful Soup to find the elements you want
# movies_today = soup.find('div', {'id': 'today'}).find_all('div', {'class': 'tx-studio-movies-list---movie'})
#
# for movie in movies_today:
#     title = movie.find('div', {'class': 'title'}).text
#     playtimes = [pt.text.strip() for pt in movie.find('div', {'class': 'playtimes'}).find_all('span', {'class': 'playtime'})]
#     print(f'Movie: {title}')
#     print(f'Playtimes: {playtimes}')

from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from time import sleep


path_to_chromedriver = 'F:\Programme\chromedriver\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = "https://www.studio-filmtheater.de/#calendar"

browser.get(url)

sleep(5)

soup = BeautifulSoup(browser.page_source, 'html.parser')

browser.quit()

# Find each day's schedule
days = soup.select('div[id^="showtag-"]')

for day in days:
    # Get the date from the UNIX timestamp in the id
    timestamp = int(day['id'].split('-')[1])
    date = datetime.utcfromtimestamp(timestamp).strftime('%A, %d. %B %Y')

    # And find the movies and playtimes
    movies_today = day.find_all('div', {'class': 'tx-studio-movies-list---movie'})

    for movie in movies_today:
        title = movie.find('div', {'class': 'title'}).text
        playtimes = [pt.text.strip() for pt in
                     movie.find('div', {'class': 'playtimes'}).find_all('span', {'class': 'playtime'})]

        # convert timestamps to human readable format
        playtimes_readable = []
        for pt in playtimes:
            time, timestamp = pt.split()
            timestamp = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            playtimes_readable.append((time, timestamp))

        print(f'Date: {date}')
        print(f'Movie: {title}')
        print(f'Playtimes: {playtimes_readable}')
        print("---------")
