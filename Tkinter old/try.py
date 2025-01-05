# class User:
#     def __init__(self,login,password,fio):
#         self._login = login
#         self._password = password
#         self._fio = fio
#     def check_password(self,password):
#         return password == self._password
#     def check_login(self,login):
#         return login==self._login
#     def get_name(self):
#         return self._fio
#     def get_login(self):
#         return self._login

# class Users:
#     def __init__(self):
#         self._users={
#             'ivanov':'123456',
#             'misterBean':'123qwe'
#         }
#     def checkLogin(self,login):
#         if login in self._users:
#             return 
#         return login in self._users

#     def checkPassword(self,login,password):
#         if self.checkLogin(login)==True:
#             return self._users[login]==password
#         else:
#             return 'Incorrect Login'
    
# a=Users()
# print(a.checkLogin('ivanov'))
# print(a.checkPassword(123,52))