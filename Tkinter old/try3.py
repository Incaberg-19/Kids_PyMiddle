import tkinter as tk
from config import *

main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")


var=[1]
label=tk.Label(main_window,text=var)

def addNumber(spisok,label):
    spisok[0]=spisok[0]+1
    label.config(text=spisok[0])


button=tk.Button(main_window,text='Прибавить 1',command=lambda: addNumber(var,label))


button.pack()
label.pack()

main_window.mainloop()


def changeVar(a):
    a=a+1

a=5
changeVar(a)
print(a) # выведется 5

def changeListVar(a):
    a[0]=a[0]+1

a=[5]
changeListVar(a)
print(a[0]) # выведется 6