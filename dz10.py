import sqlite3
conn = sqlite3.connect('weather.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS weather (
    date TEXT,
    time TEXT,
    temperature REAL
)
''')
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup
response = requests.get('https://ua.sinoptik.ua/погода-київ')
soup = BeautifulSoup(response.text, 'html.parser')
temperature = soup.find('p', class_='today-temp').text.strip()
temperature = float(temperature.replace('°', ''))

import sqlite3
from datetime import datetime
conn = sqlite3.connect('weather.db')
now = datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')
conn.execute('INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)', (date, time, temperature))
conn.commit()
conn.close()


