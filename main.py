import telebot
from telebot import types

import rem_of_div
import sum
import sub
import mult
import power
import div
import int_div
import exceptions
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log', encoding='utf-8')

bot = telebot.TeleBot("5790233525:AAGuuYr_sTvKRYS_8HUZ_LAep1bRi_NupCU")


@bot.message_handler(commands=['start'])
def start(message):
    logging.info('Start bot')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(f'/rational_numbers')
    button2 = types.KeyboardButton(f'/complex_number')
    markup.add(button1, button2)
    send_msg = f'Привет, {message.from_user.first_name}. Это бот-калькулятор! С какими числами будем работать?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['rational_numbers'])
def ration(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ rational_numbers')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f'/summa')
    button2 = types.KeyboardButton(f'/subtraction')
    button3 = types.KeyboardButton(f'/multiplication')
    button4 = types.KeyboardButton(f'/pow')
    button5 = types.KeyboardButton(f'/square_root')
    button6 = types.KeyboardButton(f'/division')
    button7 = types.KeyboardButton(f'/integer_division')
    button8 = types.KeyboardButton(f'/remainder_of_division')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    send_msg = f'Какую операцию будем производить?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['complex_number'])
def ration(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ rational_numbers')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f'/summa_comp')
    button2 = types.KeyboardButton(f'/subtraction_comp')
    button3 = types.KeyboardButton(f'/multiplication_comp')
    button4 = types.KeyboardButton(f'/pow_comp')
    button5 = types.KeyboardButton(f'/square_root_comp')
    button6 = types.KeyboardButton(f'/division_comp')
    markup.add(button1, button2, button3, button4, button5, button6)
    send_msg = f'Какую операцию будем производить?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['summa'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ summa')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['subtraction'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ subtraction')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['integer_division'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ integer_division')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['multiplication'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ multiplication')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['division'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ division')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['remainder_of_division'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ remainder_of_division')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['square_root'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ square_root')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 1 число'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['pow'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ pow')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел. Для вещественных чисел разделитель точка (3.5)'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['summa_comp'])
def summa_comp(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ summa_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['subtraction_comp'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ subtraction_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['multiplication_comp'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ multiplication_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['pow_comp'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ pow_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 3 числа: действительную затем мнимую части 1-го числа, потом степень.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['square_root_comp'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ square_root_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 2 числа: действительную затем мнимую части комплексного числа.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['division_comp'])
def summa(message):
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ division_comp')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def addition(message):
    get_msg_bot = message.text.split()
    logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ numbers = {get_msg_bot}')
    if operation == ['/summa']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sum.sum(a, b)
            send_msg = f'{a} + {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/subtraction']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sub.sub(a, b)
            send_msg = f'{a} - {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/multiplication']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = mult.mult(a, b)
            send_msg = f'{a} * {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/pow']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = power.power(a, b)
            send_msg = f'{a} ** {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/division']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = div.div(a, b)
            send_msg = f'{a} / {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/square_root']:
        a = exceptions.square_root(get_msg_bot)
        print(a)
        if a == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = power.power(a, 0.5)
            send_msg = f'{a} ** 0.5 = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/integer_division']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = int_div.int_div(a, b)
            send_msg = f'{a} // {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/remainder_of_division']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = rem_of_div.rem_of_div(a, b)
            send_msg = f'{a} % {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/summa_comp']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sum.sum(a, b)
            send_msg = f'{a} + {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/subtraction_comp']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sub.sub(a, b)
            send_msg = f'{a} - {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/multiplication_comp']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = mult.mult(a, b)
            send_msg = f'{a} * {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/pow_comp']:
        a, b = exceptions.complex_pow(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = power.power(a, b)
            send_msg = f'{a} ** {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    elif operation == ['/square_root_comp']:
        a = exceptions.complex_square(get_msg_bot)
        if a == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = power.power(a, 0.5)
            send_msg = f'{a} ** 0.5 = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')
    
    elif operation == ['/division_comp']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Упс!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = div.div(a, b)
            send_msg = f'{a} / {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        logging.info('End bot')

    send_msg = f'Для нового запроса введите команду /start'
    bot.send_message(message.chat.id, send_msg)

bot.polling(non_stop=True)
