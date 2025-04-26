import random
from pyzipper import *
import os
from tkinter import *

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

def new_zip(name, password):
    f = AESZipFile(f'{name}.zip', 'w', compression=ZIP_DEFLATED, encryption=WZ_AES)
    f.pwd = password.encode('utf-8')
    f.write(f'{name}_password.txt')
    os.remove(f'{name}_password.txt')

name = input('Введи имя пользователя: ')
password = input('Введи пароль: ')
new_chel(f'{name}_password')
com1 = int(input('Если вы хотите добавить пароль, введите 1: '))

if com1 == 1:
    social = input('вводи сервисы, для которых ты хочешь сделать пароль: ')
    while social != '':
        new_pass(f'{name}_password', social)
        print(f'Ваш пароль для {social} - {psw}')
        social = input('следующий сервис: ')
new_zip(name, password)