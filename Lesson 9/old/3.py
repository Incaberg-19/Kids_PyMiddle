# 1. Добавляем автоматическое перемещение змейки.
# 2. Создаём на поле фрукты.

import pygame
import sys

# Фрукты
# кушание фруктов (змейка достигает фрукт и фрукт пропадает)


WINDOW_SIZE = (800, 600)
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
LIGHT_GREEN_COLOR = (51,255,51)


class Fruits:
    def __init__(self):
        self._square_x, self._square_y = 100, 100
        self.color = LIGHT_GREEN_COLOR

        self._width = 30
        self._height = 30

        self._x = 0
        self._y = 0


    def getSizes(self):
        return self._width,self._height
    
    def getCoords(self):
        return self._square_x,self._square_y


def control(keys):
    returnValue = None
    if keys[pygame.K_LEFT]: returnValue = 'LEFT'
    if keys[pygame.K_RIGHT]: returnValue = 'RIGHT'
    if keys[pygame.K_UP]: returnValue = 'UP'
    if keys[pygame.K_DOWN]: returnValue = 'DOWN'
    return returnValue

class Snake:
    def __init__(self):
        self.previousAction = 'RIGHT'
        # Начальная позиция квадрата
        self._square_x, self._square_y = 100, 100

        self._width = 50
        self._height = 50

        self.color = BLACK_COLOR

    def mooving(self,action):

        if action==None: # если сейчас клавиша не нажата
            action = self.previousAction # то текущее действие равно прошлому
        else: # иначе
            self.previousAction = action # запоминаем текущее действие

        if action=='LEFT' and self._square_x > 0:
            self._square_x -= 5 
        if action=='RIGHT' and self._square_x < 750: # WINDOW_SIZE[0] = 800, 800 - 50 (ширина квадрата) = 750
            self._square_x += 5
        if action=='UP' and self._square_y > 0:
            self._square_y -= 5
        if action=='DOWN' and self._square_y < 550:
            self._square_y += 5

    def getCoords(self):
        return self._square_x,self._square_y
    
    def getSizes(self):
        return self._width,self._height

class Main:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()
        self.WINDOW_SIZE = WINDOW_SIZE
        # Создание окна
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        self.snake = Snake()

        self.background_color = WHITE_COLOR

    def gameLoop(self):

        # Цикл игры
        while True: 
            for event in pygame.event.get(): # получаем действия от игрока
                if event.type == pygame.QUIT: # если был нажат крестик 
                    pygame.quit() # выйти из библиотеки
                    sys.exit() # завершить работу программы
    
            
            # Обновляем позицию квадрата. Движение по координатам.
            keys = pygame.key.get_pressed() # Получаем состояние всех клавиш
            self.snake.mooving(control(keys))
        
            self.screen.fill(self.background_color) 
            
            pygame.draw.rect(self.screen, self.snake.color, (*self.snake.getCoords(), *self.snake.getSizes()))
            
            pygame.display.flip() 

            # Ограничиваем скорость обновления до 60 FPS
            pygame.time.Clock().tick(60) 

if __name__ == '__main__':
    Main().gameLoop()
