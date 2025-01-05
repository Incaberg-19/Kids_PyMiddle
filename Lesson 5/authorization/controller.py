# from model.data import Model
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setController(self)

    def authorizationUser(self,login,password):
        user = self.model.getUserByLogin(login.strip())
        message=''
        if user==None:
            message='Неверный логин или пароль'
        else:
            if user.checkPassword(password.strip())==True:
                message = f'Вход успешен! Здравствуйте, {user.getName()}!'
            else:
                message = 'Неверный логин или пароль'
        return message
    
    def startApp(self):
        self.view.windowStart()
