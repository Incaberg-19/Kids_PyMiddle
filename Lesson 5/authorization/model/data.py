from .user import User

class Model:
    def __init__(self):
    # создаём словарь где элементы будут логин:экземпляр
        self.usersDictionary = {
            "login1" : User("login1","VK1-Bg","Михаил Ануфрев"),
            "Harry123" : User("Harry123", "T9no-U", "Гарри Страйков"),
            "Amelia2015" : User("Amelia2015", "11_BNs", "Амелия Джугашвили"),
        }

    def getUserByLogin(self,login):
        return self.usersDictionary.get(login)
# Для получения нужной записи вызовем метод get словаря usersDictionary,
# данный метод имеет преимущество над методом прямого получения по ключу,
# потому что является безопасным, а в случае отсутствия ключа в словаре
# метод вернет значение None.