import tkinter as tk

'''
В Tkinter существуют два основных типа всплывающих окон:
MessageBox и Toplevel. 
MessageBox - маленькое всплывающее окно для уведомлений без функционала.
Toplevel - всплывающее окно которое можно настраивать: вставлять в него кнопки,
какие-то действия.
'''


#Создание корневого окна
root = tk.Tk()
root.title("Основное окно")
root.geometry("300x200")

# Функция для открытия всплывающего окна
def open_popup():
    popup_window = tk.Toplevel(root)
    popup_window.title("Всплывающее окно")
    popup_window.geometry("300x100")

    label = tk.Label(popup_window, text="Это всплывающее окно")
    label.pack(pady=20)

    close_button = tk.Button(popup_window, text="Закрыть", command=popup_window.destroy)
    close_button.pack()

# Создание кнопки для открытия всплывающего окна
open_button = tk.Button(root, text="Открыть всплывающее окно", command=open_popup)
open_button.pack(pady=20)

# Запуск приложения
root.mainloop()