from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *


def scraping(first_name="", last_name=""):

    base_url = "http://phonebook.fiu.edu/"
    url = base_url + "?q={}+{}+&button=Submit".format(first_name, last_name)

    r = requests.get(url)
    html = r.content.decode()
    soup = BeautifulSoup(html, "html.parser")

    try:
        next_url = soup.select_one("div.column.name > a").get("href")
        r = requests.get(urljoin(base_url, next_url))
        html = r.content.decode()
        soup = BeautifulSoup(html, "html.parser")
    except:
        phone_num = ""
        email = ""
        print(phone_num)
        print(email)
        return [phone_num, email]

    try:
        email = soup.select_one("div.the-content > section > section:nth-of-type(4)").text.strip()
    except:
        email = ""
    try:
        phone_num = soup.select_one("div.the-content > section > section:nth-of-type(6)").text.strip()
    except:
        phone_num = ""

    print(phone_num)
    print(email)

    return [phone_num, email]

# scraping(first_name="DEBORAH", last_name="ABEL")
scraping(first_name="PHILIP", last_name="ABBOTT")