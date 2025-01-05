import tkinter as tk
from config import *
main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
#Создание текст бокса
textBox = tk.Text(main_window, width=15, height=1) # создаём текст. окно куда можно писать
textBox.pack()
#Создание кнопки
button1 = tk.Button(main_window, text="Сказать привет",\
                   command=lambda:print('Hello',textBox.get(1.0,tk.END)))
#В качестве аргументов в метод get необходимо указать начало и конец,
#откуда будем брать данные. В качестве начала укажем 1.0 в качестве конца укажем
#tk.END это константа, обозначающая конец текстового поля.
#позиции 1.0 (начала) до tk.END (конца).
button1.pack()


# Ключевые моменты:
# Выбор метода зависит от того, как вы хотите организовать ваши элементы GUI.
# Метод place() предоставляет наибольший контроль над позиционированием, 
# но может быть сложнее использовать для сложных макетов.
# Метод grid() удобен для создания таблицоподобных макетов.
# Метод pack() прост в использовании, но менее гибкий при необходимости 
# точного позиционирования.
button2 = tk.Button(main_window, text="Сказать привет",\
                   command=lambda:print('Hello',textBox.get(1.0,tk.END)))
button2.pack(side=tk.LEFT) #left right top bottom

button3 = tk.Button(main_window, text="Сказать привет",\
                   command=lambda:print('Hello',textBox.get(1.0,tk.END)))
button3.place(x=100,y=100) # по кординатам

main_window.mainloop()