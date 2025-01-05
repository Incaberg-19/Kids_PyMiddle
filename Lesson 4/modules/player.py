class Player:
    def __init__(self,name,role,health,damage):
        self._name=name
        self._role=role
        self._health=health
        self._damage=damage

    def getName(self):
        return self._name

    def getDamage(self):
        return self._damage
    
    def getHealth(self):
        return self._health
    
    def setHealth(self,health):
        self._health=health
    
    def getInfo(self):
        return f'Игрок {self._name}, {self._role}, {self._health} хп, {self._damage} урон'