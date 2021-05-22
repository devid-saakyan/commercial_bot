import telebot
from time import sleep
from bs4 import BeautifulSoup
import requests
token = '1790070240:AAH4qSR3T2gbh-HCEH9ZR1FXNjL812W6-qU'
bot = telebot.TeleBot(token=token)
counts = [17,7,3,0,5]
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
    page = requests.get(url1, headers = headers, timeout = 5)
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
    page = requests.get(url1, headers=headers, timeout=(3.05, 27))
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_='-text-orange')[0].text
    print(a)
    return int(str(a).split(' ')[0])

def isr():
    url1 = 'https://www.lsr.ru/msk/'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
    page = requests.get(url1, headers=headers, timeout = 2)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find_all(class_='b-mini-search__submit b-btn j-search-submit')[1]
    return int(str(a.text).split(' ')[1])

while True:
    new_counts = [pik(),ingrad(),samolet_auction(),fsk(),isr()]
    print(counts, new_counts)
    if counts != new_counts:
        if counts[0] < new_counts[0]:
            print(11)
            bot.send_message(719274325, 'Пополнение в сайте ПИК')
            bot.send_message(255056634, 'Пополнение в сайте ПИК')
        if counts[1] < new_counts[1]:
            bot.send_message(719274325, 'Пополнение в сайте ИНГРАД')
            bot.send_message(255056634, 'Пополнение в сайте ИНГРАД')
        if counts[2] < new_counts[2]:
            bot.send_message(719274325, 'Пополнение в аукционах сайта САМОЛЕТ')
            bot.send_message(255056634, 'Пополнение в аукционах сайта САМОЛЕТ')
        if counts[3] < new_counts[3]:
            bot.send_message(719274325, 'Пополнение в сайте ФСК')
            bot.send_message(255056634, 'Пополнение в сайте ФСК')
        if counts[4] < new_counts[4]:
            bot.send_message(719274325, 'Пополнение в сайте ИСР')
            bot.send_message(255056634, 'Пополнение в сайте ИСР')
    counts = new_counts
    sleep(60)


bot.polling()
