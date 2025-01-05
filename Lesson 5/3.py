import tkinter as tk
from config import *
main_window = tk.Tk() # инициализируем базовый класс Tk который и станет главным окном
main_window.title(TITLE) # установка имени окна
main_window.geometry(f"{WIDTH}x{HEIGHT}") # установка размеров окна
# Есть переменная со значением 0. Задачи:
# 1) получить от пользователя другое число.
# 2) создать 2 кнопки - первая будет означать что два числа нужно сложить, вторая - вычесть.
# Причём в обоих случаях нужно брать модуль от результата математического действия.
# Выводить переменную на экран.

def addValue():
    number = userText.get(1.0,tk.END).strip()
    if len(number)!=0:
        global var
        var=var+int(number)
        label.config(text=var)

def subValue():
    number = userText.get(1.0,tk.END).strip()
    if len(number)!=0:
        global var
        var=var-int(number)
        label.config(text=var)

var = 0 
userFont = ('Helvetica', 24)
label=tk.Label(main_window,text=var,font=userFont,width=10,height=10)
label.place(relx=0.50, rely=0.10, anchor='center')

userText=tk.Text(main_window,width=13,height=1)
userText.place(relx=0.50, rely=0.20, anchor='center')

addButton = tk.Button(main_window, text="Прибавить", command=addValue,width=12,height=3)
addButton.place(relx=0.40, rely=0.30, anchor='center')

addButton = tk.Button(main_window, text="Вычесть", command=subValue,width=12,height=3)
addButton.place(relx=0.60, rely=0.30, anchor='center')


main_window.mainloop()