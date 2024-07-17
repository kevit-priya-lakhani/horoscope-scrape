import requests
from bs4 import BeautifulSoup

def scrape_data(sign,day):
    ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
    }
    sign_index=ZODIAC_SIGNS[sign]
    source=f'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={sign_index}&laDate={day}'
    source=requests.get(source).text
    soup=BeautifulSoup(source,'lxml')
    p=soup.find('p')
    # ans=main.text
    # {'grid' ,'grid-right-sidebar', 'primis-rr'}
    # day2=main.strong.text
    print(f'{sign} Predicitons')
    # print('Date: ',p.strong.text)
    print('Predictions: ',p.text)


sign=input("Enter you sun sign: ")
date=int(input('Enter date you want to check (YYYYMMDD)'))
scrape_data(sign,date)


