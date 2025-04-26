
from telebot import *
import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
length = 12
chars += digits
chars += lowercase_letters
chars += uppercase_letters
chars += punctuation
for c in 'il1Lo0O':
    chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

def new_chel(id):
    f = open(id+'.txt', 'w', encoding='utf-8')
    f.close()

def new_pass(id, social):
    f = open(id+'.txt', 'a', encoding='utf-8')
    global psw
    psw = generate_password(12, chars)
    f.write(social + ' - ' + psw+'\n')
    f.close()
    return psw

def show_pass(id):
    f = open(id+'.txt', encoding='utf-8')
    return f.read()

bot = telebot.TeleBot('7700671641:AAE7BNeD3H7q8jVBBgw6mpKXutLxgGghgsM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton ("Новый пароль")
    btn2 = types.KeyboardButton ("Мои пароли")
    #btn5 = types.KeyboardButton ("Удалить историю чата")
    markup.row(btn1, btn2)
    #markup.row(btn5)
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}, данный бот предназначен для создания безопасного пароля', reply_markup=markup)
    new_chel(str(message.from_user.id))
    markup_2 = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton('Скачать приложение на ПК',callback_data='download_app')
    btn4 = types.InlineKeyboardButton('Что за приложение, и как оно работает?',callback_data='about_app')
    markup_2.row(btn3, btn4)
    bot.send_message(message.chat.id,f'для более безопасного создания и хранения пароля вы можете скачать приложение', reply_markup=markup_2)
    
@bot.callback_query_handler(func=lambda call: call.data == 'about_app')
def callback_about(call):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Скачать приложение на ПК',callback_data='download_app')
    markup.row(btn)
    bot.send_message(
        call.message.chat.id, f'Данное приложение создано для создания безопасного создания и хранения пароля. Оно не подключено к интернету или к другим сетям, поэтому дистанционно его не возможно взломать. Для входа в программу нужно ввести пароль, чтобы посмотреть пароли для других сервисов.', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: call.data == 'download_app')
def callback_app(call):
    zip_file_path = 'SafetyPassword.zip'
    with open(zip_file_path, 'rb') as zip_file:
        bot.send_document(call.message.chat.id, zip_file)
    
@bot.message_handler()
def click(message):
    if message.text.lower() == 'новый пароль' or message.text.lower() == 'cоздать ещё пароль':
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Введите сервис для которого вы хотите получить пароль')
    elif message.text.lower() == 'мои пароли':
        bot.send_message(message.chat.id, show_pass(str(message.from_user.id)))
    elif message.text.lower() in open(str(message.from_user.id) + '.txt', encoding='UTF-8').read():
            bot.reply_to(message, 'Этот пароль уже был создан для данного сервиса')
    #elif message.text.lower() == 'удалить историю чата':
        #while True:
            #bot.delete_message(message.chat.id, int(message.message_id) - 1)
    else:
        new_pass(str(message.from_user.id), message.text.lower())
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Cоздать ещё пароль", callback_data='create_new')
        markup.row(btn1)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Ваш пароль для {message.text} - {psw}', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'create_new')
def callback_new(call):
    bot.send_message(call.message.chat.id, f'{call.from_user.first_name}, Введите сервис для которого вы хотите создать пароль')
    
    
   
bot.polling(non_stop=True)  