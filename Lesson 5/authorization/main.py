from model.data import Model
from view import View
from controller import Controller

class App:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model,self.view)
    def startApp(self):
        self.controller.startApp()
        
if __name__ == '__main__':
    app = App()
    app.startApp()
