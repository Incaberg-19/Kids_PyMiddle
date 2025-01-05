#User.py
class User:
    def __init__(self,login,password,fio):
        self._login = login
        self._password = password
        self._fio = fio
    def check_password(self,password):
        return password == self._password
    def check_login(self,login):
        return login==self._login
    def get_name(self):
        return self._fio
    def get_login(self):
        return self._login

allOfUsers=[]
while True:
    print('Вы зарегестрированы?')
    user=input()
    if user=='Да':
        log=input("Введите логин:")
        password=input("Введите пароль:")
        for element in allOfUsers:
            if element.check_login(log)==True:
                if element.check_password(password)==True:
                    print(f'Пользователь {element.get_name()} найден!')
                    break
                else:
                    print('Неверный пароль')
        else:
            print('Пользователь с таким логином не найдено')
    else:
        log=input("Введите логин:")
        password=input("Введите пароль:")
        fio=input("Введите ФИО:")
        allOfUsers.append(User(log,password,fio))
        print(allOfUsers)

