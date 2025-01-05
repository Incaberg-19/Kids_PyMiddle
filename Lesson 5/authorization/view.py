import tkinter as tk
from config import *
class View:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title(TITLE)
        self.mainWindow.geometry(f"{WIDTH}x{HEIGHT}")

        self.LoginLabel = tk.Label(self.mainWindow, text="Логин")
        self.loginText = tk.Text(self.mainWindow, width=15, height=1)

        self.passwordLabel = tk.Label(self.mainWindow, text="Пароль")
        self.passwordText = tk.Text(self.mainWindow, width=15, height=1)

        self.labelInfoAuth = tk.Label(self.mainWindow,text='Авторизация')

        self.authButton = tk.Button(self.mainWindow, text="Войти",command=self.processButton)
        

    def processButton(self):
        outputString=self.controller.authorizationUser(self.loginText.get(1.0, tk.END), self.passwordText.get(1.0, tk.END))
        self.labelInfoAuth.config(text=outputString)    

    def setController(self,controller):
        self.controller=controller
    
    def outputObjects(self):

        self.LoginLabel.pack()
        self.loginText.pack()

        self.passwordLabel.pack()
        self.passwordText.pack()

        self.labelInfoAuth.pack()

        self.authButton.pack()

    def windowStart(self):
        self.outputObjects()
        self.mainWindow.mainloop()