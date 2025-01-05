import tkinter as tk
from config import *

class menu:
    def __init__(self,main_window):
        # self.users=Users()
        self.users={
            'ivanov':'123qwe',
        }
        self.window=main_window
        self.action=False
        self.pastAction=False
        self.font_header = ('Arial', 15)
        self.main_label = tk.Label(self.window, text='\nВы зарегистрированы?', font=self.font_header)
        self.button1 = tk.Button(self.window, text="Да",width=8,height=3,command=self.setActionTrue)
        self.button2 = tk.Button(self.window, text="Нет",width=8,height=3,command=self.setActionFalse)
        self.main_label.pack()
        # self.button1.pack(anchor="center")
        # self.button2.pack(anchor="center")
        # self.button1.pack(side=tk.LEFT,anchor="n",relx=0.5, rely=0.5)
        # self.button2.pack(side=tk.RIGHT,anchor="n")
        self.button1.place(relx=0.55, rely=0.16, anchor='center')
        self.button2.place(relx=0.45, rely=0.16, anchor='center')
        # self.button2.pack(pady=(10, 10))
        # self.main_label.place(x=100,y=100)
        # self.button1.place(x=400,y=110)
        # self.button2.place(x=500,y=110)

    def setActionTrue(self):
        self.pastAction=self.action # создано для предотвращения наложения
        self.action = True  
        if self.pastAction==False:
            self.label_login = tk.Label(self.window, text="Логин:", font=self.font_header)
            self.label_password = tk.Label(self.window, text="Пароль:", font=self.font_header)

            self.loginBox = tk.Text(self.window, width=15, height=1)
            self.passwordBox=tk.Text(self.window, width=15, height=1)

            self.loginBox.place(relx=0.50, rely=0.30, anchor='center')
            self.label_login.place(relx=0.35, rely=0.30, anchor='center')

            self.passwordBox.place(relx=0.50, rely=0.35, anchor='center')
            self.label_password.place(relx=0.35, rely=0.35, anchor='center')

            self.buttonSave = tk.Button(self.window, text="Сохранить данные?",width=20,height=3,command=self.saveInfo)
            self.buttonSave.place(relx=0.50, rely=0.45, anchor='center')

    def setActionFalse(self):
        self.pastAction=self.action
        self.action = False
        if self.pastAction==True:
            self.loginBox.destroy()
            self.passwordBox.destroy()
            self.label_password.destroy()
            self.label_login.destroy()
            self.buttonSave.destroy()

    def saveInfo(self):
        self.users[self.loginBox.get(1.0,tk.END)]=self.passwordBox.get(1.0,tk.END)
        print(self.users)


def  main():
    main_window = tk.Tk()
    # main_window.resizable(False, False) # Запрещаем изменять размер окна
    main_window.title(TITLE)
    main_window.geometry(f"{WIDTH}x{HEIGHT}")
    authorization=menu(main_window)
    main_window.mainloop()

if __name__ == "__main__":
    main()