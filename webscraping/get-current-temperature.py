from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

from datetime import date
import calendar

def dayofweek() -> str:
    day = date.today()
    return calendar.day_name[day.weekday()]

def get_weather_temperature(city: str):

    prefs = {
        'intl.accept_languages': 'en-US'
    }
    
    #OR
    #prefs = {
    #    "translate_whitelists": {'nl':'en'},
    #    "translate": {"enabled": "true"}
    #}

    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--lang=en-US')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome(options=options)

    search_url = "https://www.google.com/search?q=weather+" + city

    driver.get(search_url)
    time.sleep(30)
    page_html = driver.page_source
    driver.close()

    # Retrieve HTML tags and metadata
    soup = BeautifulSoup(page_html, 'html.parser')
    result = soup.find_all('div', attrs={'class': "R3Y3ec rr3bxd", 'class': 'wob_df', 'class':'wob_df wob_ds', 'data-wob-di':'0'})

    dayofweek = ''
    temperature = ''
    weathertype = ''

    for d in result:
        dayofweekdata = d.find('div', attrs={'class':'Z1VzSb'})
        temperaturedata = d.find('span', attrs={'class':'wob_t'})
        weathertypedata = d.find('img', attrs={'class':'YQ4gaf zr758c'})
        #print(dayofweekdata)
        #print(temperaturedata)
        #print(weathertypedata)
        
        dayofweek = [c.get_text(strip=True) for c in dayofweekdata]
        temperature = [b.get_text(strip=True) for b in temperaturedata]
        weathertype = weathertypedata['alt']
        #print(dayofweek[0])
        #print(temperature[0])
        #print(weathertype)

    print("Today's Temperature: {} {} degrees fahrenheit".format(dayofweek[0], temperature[0]))
    if weathertype == "Light rain":
        print("Its {}! You might need umbrella.".format(weathertype))
    elif weathertype == "Rain":
        print("Its {}! You need umbrella.".format(weathertype))
    else:
        print("Its {}! Enjoy outside.".format(weathertype))


if __name__ == "__main__":
    get_weather_temperature('Chicago')