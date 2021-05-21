from bs4 import BeautifulSoup
import requests

def pik():
    url1 = 'https://www.pik.ru/projects/commercial'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    page = requests.get(url1, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_= 'sc-dwfUOf bOVjqe', type = 'primary')[0]
    b = int(str(a.text).split(' ')[0])
    return b

def ingrad():
    url1 = 'https://www.ingrad.ru/commercial/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrodiv78.0.3904.70 Safari/537.36'}
    page = requests.get(url1, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_='col')
    return len(a)

def samolet_auction():
    url1 = 'https://auction.samolet.ru/catalog'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
    page = requests.get(url1, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_ = 'cell_3umcx')
    return len(a)

def fsk():
    url1 = 'https://fsk.ru/kommercheskaya-nedvizhimost'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
    page = requests.get(url1, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_='-text-orange')[0].text
    return int(str(a).split(' ')[0])

def isr():
    url1 = 'https://www.lsr.ru/msk/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
    page = requests.get(url1, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_='b-mini-search__submit b-btn j-search-submit')[1]
    return int(str(a.text).split(' ')[1])
