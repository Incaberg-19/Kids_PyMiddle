import tkinter as tk
from config import *


main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")

global var
var=0

label=tk.Label(main_window,text=var)

def addNumber():
    global var
    var=var+1
    label.config(text=var)

button=tk.Button(main_window,text='Прибавить 1',command=addNumber)

button.pack()
label.pack()

main_window.mainloop()