import tkinter as tk
from config import *
main_window = tk.Tk() # инициализируем базовый класс Tk который и станет главным окном
main_window.title(TITLE) # установка имени окна
main_window.geometry(f"{WIDTH}x{HEIGHT}") # установка размеров окна

textBox = tk.Text(main_window, width=15, height=1) # создание текстового окна куда
# пользователь может вводить сообщение
textBox.pack() # простейший инструмент для расположения объектов на экране

# end означает конец всего текста в виджете.
# userText=textBox.get(1.0,tk.END) такая строчка не сработает потому что она не вызывается
# каждый раз при нажатии на кнопку
# "1.0":
# Это начальная позиция индекса в виджете Text.
# Означает первый символ первой строки текста.
# Состоит из двух частей: номер строки (1) и номер символа (0).


button = tk.Button(main_window, text="Сказать привет", command=lambda:print(f"Hello {textBox.get(1.0,tk.END)}"))
button.pack() # простейший инструмент для расположения объектов на экране

main_window.mainloop()