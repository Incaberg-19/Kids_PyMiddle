import tkinter as tk
from config import *
main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
#Создание текст бокса
textBox = tk.Text(main_window, width=15, height=1) # создаём текст. окно куда можно писать
#Создание кнопки
button1 = tk.Button(main_window, text="Сказать привет",\
                   command=lambda:print('Hello',textBox.get(1.0,tk.END)))
button1.grid(row=0, column=0) # сеткой
textBox.grid(row=1, column=1)

main_window.mainloop()