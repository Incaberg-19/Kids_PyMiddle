
from ..consts import *
from pygame import Rect

class Snake:
    def __init__(self):
        self._rects = [Rect(4*RECT_SIZE, 8*RECT_SIZE, RECT_SIZE, RECT_SIZE)]
        self.color = BLACK
        self.direction = 'RIGHT'  # Начальное направление

    def setDirection(self, action):
        if action in ['LEFT', 'RIGHT', 'UP', 'DOWN']:
            self.direction = action

    def moving(self):
        head = self._rects[0].copy()  # Копируем голову змеи


        if self.direction == 'LEFT': head.x -= RECT_SIZE
        if self.direction == 'RIGHT': head.x += RECT_SIZE
        if self.direction == 'UP': head.y -= RECT_SIZE
        if self.direction == 'DOWN': head.y += RECT_SIZE

        self._rects.insert(0, head)  # Добавляем новую голову
        self._rects.pop(-1)  # Удаляем последний сегмент

    def grow(self):
        # Увеличиваем змейку, добавляя сегмент в конец
        rect = self._rects[-1].copy()
        self._rects.append(rect)

    def getListRects(self):
        return self._rects