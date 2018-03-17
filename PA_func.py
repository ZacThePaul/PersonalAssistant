import requests
from bs4 import BeautifulSoup
import sqlite3
import time as t

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


def hello():
    print('...')
    t.sleep(2)
    initialize = ['Initiating startup sequence', ' ...', ' ...']
    for i in initialize:
        print(i, end='', flush=True)
        t.sleep(1)
    t.sleep(1)
    print('\n...')
    t.sleep(1)
    print('\n \n|| Welcome to your Personal Assistant ||')
    print(
        'I am a Python program written by ZacThePaul. If you have questions about my mind, at any prompt please enter \'iMind\'.')
    print('You will be given a link to Github where my brains are stored!')
    print('\nPlease take some time to chat with me, so I can get to know you.')
    t.sleep(1)


def cnn(keyword, sites):
    titlefound = []
    url = 'https://www.cnn.com/world'
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    articles = soup.find_all('h3', {'class': 'cd__headline'})

    print('Here are some articles on {} containing the word \'{}\':'.format(sites, keyword))
    print('\n')

    for article in articles:
        title = article.find('span').text
        link = article.find('a')['href']
        if keyword in title:
            if title not in titlefound:
                if 'http' not in link:
                    print(title, 'http://www.cnn.com' + link)
                    titlefound.append(title)
                else:
                    print(title, link)
                    titlefound.append(title)
            elif title in titlefound:
                continue

    if len(titlefound) == 0:
        print('Whoops! Sorry about that, it looks like your search came up empty!')


def npr(keyword, sites):
    url = 'https://www.npr.org/sections/news/'
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    kw = keyword.title()
    titleforfound = []  # Arbitrary list to help determine if the program has found anything
    articles = soup.find_all('article', {'class': 'item has-image'})

    print('Here are some articles on {} containing the word \'{}\': '.format(sites, keyword))
    print('\n')

    for article in articles:  # This singles out each individual post in a collection of posts (articles)
        title = article.find('h2').find('a').text  # This specifies that I want the title only, no HTML
        link = article.find('a')['href']  # This finds the link of the specific article
        if kw in title:  # this analyzes the titles and compares the keyword to each individual word
            print(title, '~', link)
            titleforfound.append(title)  # adding to list to let the program know something has been found

    if len(titleforfound) == 0:  # if the program didn't find anything
        print('Whoops! Sorry about that, it looks like your search came up empty!')


def fox(keyword, sites):
    url = 'https://www.cnn.com/world'  # url that is being scraped
    soup = BeautifulSoup(requests.get(url).content, "lxml")  # retrieves content from the url
    titlefound = []
    articles = soup.find_all('h3', {'class': 'cd__headline'})

    print('Here are some articles on {} containing the word \'{}\':'.format(sites, keyword))
    print('\n')

    for article in articles:
        title = article.find('span').text
        link = article.find('a')['href']
        if keyword in title:
            if title not in titlefound:
                if 'http' not in link:
                    print(title, 'http://www.cnn.com' + link)
                    titlefound.append(title)
                else:
                    print(title, link)
                    titlefound.append(title)
            elif title in titlefound:
                continue

    if len(titlefound) == 0:
        print('Whoops! Sorry about that, it looks like your search came up empty!')


def headlinescanner():

    NPR = ['NPR', 'npr', 'Npr', 'n.p.r.']
    CNN = ['CNN', 'cnn', 'C.N.N.']
    FOX = ['fox', 'FOX', 'Fox']

    keyword = input('What are you looking for?')
    sites = input('What website would you like to pull from?')

    if sites in NPR:
        P.npr(keyword, sites)
    elif sites in CNN:
        P.cnn(keyword, sites)
    elif sites in FOX:
        P.fox(keyword, sites)


def birthday(dob):
    cdob = dob.split('-')
    year = cdob[0]
    month = cdob[1]
    day = cdob[2]
    return month, day, year


def bdayformat(cuser_dob):
    months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
              '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    for i in months:
        if cuser_dob[0] == i:
            return months[i]


def user_age(cuser_dob):
    from datetime import date
    import datetime
    now = datetime.datetime.now()
    f_date = date(int(cuser_dob[2]), int(cuser_dob[0]), int(cuser_dob[1]))
    l_date = date(now.year, now.month, now.day)
    delta = l_date - f_date
    years = delta.total_seconds()
    cyears = years / 31557600
    return cyears


def user_weather():
    city = c.execute('SELECT city FROM user').fetchall()[0][0]
    state = c.execute('SELECT state FROM user').fetchall()[0][0]
    zip = str(c.execute('SELECT zip_code FROM user').fetchall()[0][0])
    url = 'https://www.wunderground.com/weather/us/' + state + '/' + city + '/' + zip
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    temp = soup.find_all('span', {'class': 'wu-value wu-value-to'})

    return temp[0].text


def user_location(user_name):
    uloc = c.execute('SELECT city, state, country FROM user WHERE name = (?);', (user_name,))
    return uloc


#  SQLITE FUNCTIONS  #


def create_assistant():

    c.execute("CREATE TABLE IF NOT EXISTS assistant (named INTEGER, assistant_name VARCHAR )")


def name_assistant(name):
    c.execute('INSERT INTO assistant VALUES (?, ?)', (1, name),)
    conn.commit()


def create_user():

    c.execute("CREATE TABLE IF NOT EXISTS user (name VARCHAR, dob INTEGER, city VARCHAR, state VARCHAR, zip_code VARCHAR)")  # for dob it is yyyy-mm-dd


def name_user(name):
    c.execute('INSERT INTO user VALUES (?, ?, ?, ?, ?)', (name, 0, 0, 0, 0),)
    conn.commit()


def user_dob(dob):
    c.execute('UPDATE user SET dob = (?)', (dob,))
    conn.commit()


def locate_user_city(town):
    c.execute('UPDATE user SET city = (?)', (town,),)
    conn.commit()


def locate_user_state(state):
    c.execute('UPDATE user SET state = (?)', (state,),)
    conn.commit()


def locate_user_zip(zip):
    c.execute('UPDATE user SET zip_code = (?)', (zip,))
    conn.commit()