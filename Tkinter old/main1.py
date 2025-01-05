import tkinter as tk
from config import *

class menu: 
    def __init__(self,window):
        self.var=0
        self.window=window
        self.label=tk.Label(self.window,text=self.var)
        self.button=tk.Button(main_window,text='Прибавить 1',command=self.addNumber)
        self.label.pack()
        self.button.pack()
    
    def addNumber(self):
        self.var=self.var+1
        self.label.config(text=self.var)

main_window = tk.Tk()
#создается экземпляр класса Tk, который является корневым окном приложения.
main_window.title(TITLE) # установка имени окна
main_window.geometry(f"{WIDTH}x{HEIGHT}") # установка размеров окна
m1=menu(main_window)
#main_label.pack()
#button.pack() # отобразить кнопку в окне


main_window.mainloop() #Запуск главного цикла событий (вызывает окно)

