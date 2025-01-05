from ..consts import RECT_SIZE,YELLOW
from pygame import Rect
from random import randint

class Fruit:
    def __init__(self):
        self._rect=Rect(randint(0,9)*RECT_SIZE,randint(0,19)*RECT_SIZE,RECT_SIZE,RECT_SIZE)
        self.color = YELLOW
    
    def changePosition(self):
        self._rect.x = randint(0,9) * RECT_SIZE
        self._rect.y = randint(0,19) * RECT_SIZE
    
    def getRect(self):
        return self._rect