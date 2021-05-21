import telebot
from telebot import types
from parsing import *
from time import sleep

token = '1790070240:AAH4qSR3T2gbh-HCEH9ZR1FXNjL812W6-qU'
bot = telebot.TeleBot(token=token)

counts = [19,7,4,13,5]
@bot.message_handler(commands=['start', 'stop'])
def send_hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте, Сергей\n'
                                            'Бот следит за сайтами ПИК, ИНГРАД, САМОЛЕТ, ФСР, ИСР\n'
                                            'Как только бот обнаружит новые публикации, сразу же сообщит об этом в сообщениях\n'
                                            'Ни в коем случае не остановите бот, так как он не смо;ет отправить вам сообщения')
    bot.register_next_step_handler(message, main)

def main():
    while True:
        new_counts = [pik(),ingrad(),samolet_auction(),fsk(),isr()]
        if counts != new_counts:
            if counts[0] < new_counts[0]:
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
        sleep(30)



bot.polling()