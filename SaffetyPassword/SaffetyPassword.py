from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from pyzipper import *
import os
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

def generate_password(length):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    chars += digits
    chars += lowercase_letters
    chars += uppercase_letters
    chars += punctuation
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

def new_chel(id):
    f = open(id+'.txt', 'w', encoding='utf-8')
    f.close()

def new_pass(id, social, length):
    f = open(id+'.txt', 'a', encoding='utf-8')
    global psw
    psw = generate_password(length, chars)
    f.write(social + ' - ' + psw+'\n')
    f.close()
    return psw

def show_pass(id):
    f = open(id+'.txt', encoding='utf-8')
    return f.read()

def new_zip(name, password):
    f = AESZipFile(f'{name}.zip', 'w', compression=ZIP_DEFLATED, encryption=WZ_AES)
    f.pwd = password.encode('utf-8')
    f.write(f'{name}_passwords.txt')
    os.remove(f'{name}_passwords.txt')
    
def info_btn():
    showinfo(title='Информация об использовании',\
        message=\
            f'Чтобы использовать приложение вам нужно ввести своё имя и пароль, который в последующем вы сможете использовать для открытия ZIP-файла, в котором будет txt- файл, где и будут лежать ваши пароли. Для настройки вам понадобятся ввести сервисы, где будете использовать пароль, количество символов, нажать кнопку "Создать пароль" и нажать на "Создать ZIP-файл". Всё! Ваши пароли теперь храняться с зашифровкой AES.')



    
def new_window():
    if entry_name.get() == '' and entry_pass.get() == '':
        return showerror(title='Ошибка', message='Для дальнейшей настройки, введите пароль и имя.')
    
    def add():
        social_get = entry_serv.get()
        social_lsb.insert(0, social_get)
        entry_serv.delete(0, END)
    
    def delete():
        slct = social_lsb.curselection()
        social_lsb.delete(slct[0])
        psw_lsb.delete(slct[0])
        
    def del_all():
        social_lsb.delete(0, END)
        psw_lsb.delete(0, END)
    
    def show_psw_lsb():
        if entry_length.get() == '':
            showerror(title='Ошибка', message='Введите колличество символов, которые будут в паролях')
        if social_lsb.get(0) == '':
            showerror(title='Ошибка', message='Введите сервис, к которому хотите создать пароль.')
            
        ls = []
        for i in social_lsb.get(-1, last=END):
            password = generate_password(int(entry_length.get()))
            ls.append(f'{i} - {password}')   
        psw_lsb.insert(0,*ls)
        
    def gotovo():
        file = open(get_name + '_passwords.txt', 'a', encoding='utf-8')
        for psn in psw_lsb.get(0, last=END):
            file.write(psn + '\n')
        file.close()
        new_zip(get_name, get_pass)
        quest = askyesno(title='Готово', message= f'ZIP-Файл создан, с паролем - {get_pass}.\nЗакрыть программу?')
        if quest: 
            sett.destroy()
        
        
        
            

        
    sett = Tk()
    sett.title('настройки')
    x_sett = ((sett.winfo_screenwidth() - root.winfo_reqwidth()) / 2) - 270
    y_sett = ((sett.winfo_screenheight() - root.winfo_reqheight()) / 2) - 350
    sett.wm_geometry(f'720x720+{int(x_sett)}+{int(y_sett)}')
    get_name = entry_name.get() #переменная для имени
    get_pass = entry_pass.get() #переменная для пароля
    root.destroy()
    sett.update_idletasks()
    sett.resizable(False,False)
    sett.config(bg="#212121")
    sett.grab_set()
    
    btn_style1 = ttk.Style(sett)
    btn_style1.configure(".", 
                    background="#595959", # имя стиля
                    foreground="white",   # цвет текста
                    padding=5,             # отступы, 
                    ) 
    
    btn_style12 = ttk.Style(sett)
    btn_style12.configure("My5.TSpinbox", 
                    background="#595959", # имя стиля
                    foreground="black",   # цвет текста
                    padding=5,
                    font=("Arial", 14) # отступы, 
                    ) 


    
    label_serv = ttk.Label(
        sett, text='Введите сервис', font=("Arial", 20), background="#212121", foreground='white')
    label_serv.place(x=40,y=30)
    
    entry_serv = ttk.Entry(
        sett, font=("Arial", 15), style="My2.TLabel")
    entry_serv.place(x=42,y=70, width=200, height=32)

    btn_add = Button(
        sett, text='Добавить', command=add, background='#595959', foreground='white', highlightthickness=0, bd=0)
    btn_add.place(x=42,y=105, height=30)
    
    entry_length = Spinbox(
        sett, from_=4, to=20, background="#595959", foreground='white', font=("Arial", 14), buttonbackground='#595959', highlightthickness=0, bd=0)
    entry_length.place(x=43, y=180, height=32, width=50)
    
    lable_length = ttk.Label(
        sett, text='Введите кол-во знаков в пароле', font=("Arial", 14), background="#212121", foreground='white')
    lable_length.place(x=42, y=145)
    
    social_lsb = Listbox(
        sett, font=("Arial", 14), background="#595959", selectbackground="#9fa0b5", foreground='white', highlightthickness=0, bd=0)
    social_lsb.place(x=43, y=225, width=150, height=250)
    
    btn_del = Button(
        sett, text='Удалить выбранное', command=delete, background='#595959', foreground='white', highlightthickness=0, bd=0)
    btn_del.place(x=210, y=285, height=25)
    
    btn_del_all = Button(
        sett, text='Удалить всё', command=del_all, background='#595959', foreground='white', highlightthickness=0, bd=0)
    btn_del_all.place(x=210, y=315, height=25)
    
    btn_gotovo = Button(
        sett, text='Создать пароли', command=show_psw_lsb, background='#595959', foreground='white', highlightthickness=0, bd=0)
    btn_gotovo.place(x=210, y=350, height=40)
    
    psw_lsb = Listbox(
        sett, font=("Arial", 12),background="#595959", selectbackground="#9fa0b5", foreground='white', highlightthickness=0, bd=0)
    psw_lsb.place(x=377, y=225, width=300, height=250)
    
    btn_create_zip = Button(
        sett, text='Создать zip-файл', command=gotovo, background='#595959', foreground='white', highlightthickness=0, bd=0)
    btn_create_zip.place(x=477, y=515, height=40)
    

    



root = Tk()
root.title('Приложение для создания паролей')
x_root = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2) - 67
y_root = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2) - 150
root.wm_geometry(f'270x300+{int(x_root)}+{int(y_root)}')
root.update_idletasks()
root.resizable(False,False)
icon = PhotoImage(file='SaffetyPassword/avatar3.png')
root.iconphoto(True, icon)	
root.config(bg="#212121")

label_name = Label(text='Введи имя пользователя',font=("Arial", 14), background='#212121', foreground='white')
label_name.place(x=25,y=30)

entry_name = ttk.Entry(style='My1.TLabel')
entry_name.place(x=35,y=60, width=200, height=26)



btn_style = ttk.Style()
btn_style.configure("My1.TLabel", 
                    background="#595959", # имя стиля
                    foreground="white",   # цвет текста
                    padding=5,             # отступы, 
                    )   

entry_style = ttk.Style()
entry_style.configure('Entr.TEntry',
                      background = '#595959')



label_pass = ttk.Label(text='Придумайте пароль',font=("Arial", 14), background='#212121', foreground='white')
label_pass.place(x=46,y=110)

entry_pass = ttk.Entry(style="My1.TLabel")
entry_pass.place(x=35,y=140, width=200, height=26)

btn_info = Button(text='как испальзовать приложение?', command=info_btn, background='#595959', foreground='white', highlightthickness=0, bd=0)
btn_info.place(x=50,y=220, height=27)


btn_cont = Button(text='продолжить', command=new_window, background='#595959', foreground='white', highlightthickness=0, bd=0)
btn_cont.place(x=97,y=175, height=25)

#print(entry_name.get(), entry_pass.get())



root.mainloop()


