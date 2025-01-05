from random import randint,choice
from .player import Player
def definePlayers(classes:dict,countOfPlayers)->dict:
    players=[] # создаём список игроков
    keys=list(classes.keys()) # создаём список с названиями классов
    for i in range(1,countOfPlayers+1):
        randomKey=choice(keys) # случайно выбираем класс
        hp=randint(*classes[randomKey][0]) # выбираем случайно хп
        damage=randint(*classes[randomKey][1]) # случайно дамаг
        players.append(Player(i,randomKey,hp,damage))
    return players