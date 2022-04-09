import telebot
from telebot import types
import random


bot = telebot.TeleBot("5238206960:AAGv8aw2-G-Ivy7TpehomjqreaJFJbKa-ao")

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать ID вопроса")
    btn2 = types.KeyboardButton("Рандомный вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Вас приветствует Nachalnik, чтобы узнать что я умею напиши /help", reply_markup=markup)

@bot.message_handler(commands=['question'])
def question(message):
    markup = types.ReplyKeyboardMarkup()
    with open('answer.txt', encoding='utf=8') as f:
        l=f.read()
    bot.send_message(message.chat.id, text="Вопросы для стажировки", reply_markup=markup)
    bot.send_message(message.chat.id, l,reply_markup=markup)


@bot.message_handler(commands=['help'])
def question(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, text="Начнем,  введи команду /question чтоб увидеть список всех вопросов, если у вас появились вопросы или предложения для улучшения бота введите команду /add_question, для выхода введи команду /exit", reply_markup=markup)

@bot.message_handler(commands=["add_question"])
def add_(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton( "Message the developer", url="telegram.me/lenshin15"))
    bot.send_message(message.chat.id,'Если есть предложения по изменению бота, свяжитесь с другом разработчика.',reply_markup=keyboard)


@bot.message_handler(commands=["exit"])
def exit(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEZrhiTxQdSpcP7-AenqCL1Fq2ArN0hwACfRMAAqN3qEvCWDsDiG_N4CME")


@bot.message_handler(content_types=["text"])
def message(message):
    markup = types.InlineKeyboardMarkup()
    if message.text == "Выбрать ID вопроса":
        with open('answer.txt', encoding='utf=8') as f:
            l = f.read()
        bot.send_message(message.chat.id, text="Выберите вопрос", reply_markup=markup)
        bot.send_message(message.chat.id, l, reply_markup=markup)

    if message.text == "1":
        bot.send_message(message.from_user.id, "Вопрос1:\n'В чём разница между списком и кортежом?'\nОтвет:\n'Разница между списком и кортежем заключается в том, что список объявляется в квадратных скобках и может быть изменен, в то время как кортеж объявляется в скобках и не может быть изменен.'")
    if message.text == "2":
        bot.send_message(message.from_user.id, "Вопрос2:\n'Что такое двоичный код?'\nОтвет:\n'Двоичный код – это бинарная форма представления кода определенного языка программирования'")
    if message.text == "3":
        bot.send_message(message.from_user.id, "Вопрос3:\n'Что делает компилятор?'\nОтвет:\n'Компилятор «читает» код, написанный на определенном языке программирования, и преобразует описанные команды и конструкции языка в исполняемый машинный код.'")
    if message.text == "4":
        bot.send_message(message.from_user.id, "Вопрос4:\n'Что такое массив?'\nОтвет:\n'Массив – это набор смежных областей памяти, которые хранят данные определенного типа.'")
    if message.text == "5":
        bot.send_message(message.from_user.id, "Вопрос5:\n'Зачем нужны реляционные операторы?'\nОтвет:\n'Реляционные операторы используются в программировании для сравнения значений. Результатом оценки с использованием реляционных операторов будет true или false.'")
    if message.text == "6":
        bot.send_message(message.from_user.id, "Вопрос6:\n'Зачем нужны операторы присваивания?'\nОтвет:\n'Оператор присваивания используется для сохранения значений в переменной.'")
    if message.text == "7":
        bot.send_message(message.from_user.id, "Вопрос7:\n'Что такое машинный код?'\nОтвет:\n'Машинный код – это язык программирования, который может обрабатываться напрямую процессором, без необходимости предварительной компиляции.'")
    if message.text == "8":
        bot.send_message(message.from_user.id, "Вопрос8:\n'Что такое вложенный цикл?'\nОтвет:\n'Цикл, который выполняется в теле другого цикла, является вложенным.'")
    if message.text == "9":
        bot.send_message(message.from_user.id, "Вопрос9:\n'Что такое алгоритм?'\nОтвет:\n'Алгоритм – это конечный набор шагов, которые при следовании им решают какую-то задачу.'")
    if message.text == "10":
        bot.send_message(message.from_user.id, "Вопрос10:\n'Что такое блок-схема?'\nОтвет:\n'Блок-схема – это графическое представление программы. Блок-схема помогает понять логику работы программы или ее части при проектировании.'")

    if message.text.strip() == 'Рандомный вопрос':
            with open('answer - копия.txt', encoding='utf-8') as f:
                file = f.read().split('probel')
            file1 = random.choice(file)
            bot.send_message(message.chat.id, file1)




bot.polling()
