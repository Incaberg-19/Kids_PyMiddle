class User:
    def __init__(self,login,password,fio):
        self._login = login
        self._password = password
        self._fio = fio
    def checkPassword(self,password):
        return password == self._password
    def getName(self):
        return self._fio
    def getLogin(self):
        return self._login