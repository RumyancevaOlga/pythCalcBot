import telebot
from telebot import types

import rem_of_div
import sum
import sub
import mult
import power
import div
import int_div
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log', encoding='utf-8')

bot = telebot.TeleBot("5667225862:AAGyvro8Afy_zEbujx8GiVpvuZnaYLsDVbU")


@bot.message_handler(commands=['start'])
def start(message):
    logging.info('Start bot')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(f'/rational_numbers')
    button2 = types.KeyboardButton(f'/Комплексные числа')
    markup.add(button1, button2)
    send_msg = f'Привет, {message.from_user.first_name}. Это бот-калькулятор! С какими числами будем работать?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['rational_numbers'])
def ration(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ rational_numbers')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f'/Сумма')
    button2 = types.KeyboardButton(f'/Вычитание')
    button3 = types.KeyboardButton(f'/Умножение')
    button4 = types.KeyboardButton(f'/Cтепень')
    button5 = types.KeyboardButton(f'/Извлечение_корня')
    button6 = types.KeyboardButton(f'/Деление')
    button7 = types.KeyboardButton(f'/Целочисленное_деление')
    button8 = types.KeyboardButton(f'/Остаток_от_деления')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    send_msg = f'Какую операцию будем производить?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Сумма'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Сумма')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Вычитание'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Вычитание')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Целочисленное_деление'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Целочисленное_деление')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Умножение'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Умножение')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Деление'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Деление')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Остаток_от_деления'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Остаток_от_деления')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['Извлечение_корня'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Извлечение_корня')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 1 число'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['Степень'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ Степень')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def addition(message):
    get_msg_bot = message.text.split()
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ numbers = {get_msg_bot}')
    if operation == ['/Сумма']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = sum.sum(a, b)
        send_msg = f'{a} + {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Вычитание']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = sub.sub(a, b)
        send_msg = f'{a} - {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Умножение']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = mult.mult(a, b)
        send_msg = f'{a} * {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Степень']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = power.power(a, b)
        send_msg = f'{a} ** {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Деление']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = div.div(a, b)
        send_msg = f'{a} / {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Извлечение_корня']:
        a = int(get_msg_bot[0])
        result = a ** 0.5
        send_msg = f'{a} ** 0,5 = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Целочисленное_деление']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = int_div.int_div(a, b)
        send_msg = f'{a} // {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')

    elif operation == ['/Остаток_от_деления']:
        a = int(get_msg_bot[0])
        b = int(get_msg_bot[1])
        result = rem_of_div.rem_of_div(a, b)
        send_msg = f'{a} % {b} = {result}'
        bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {result}')
        logging.info('End bot')


bot.polling(non_stop=True)
