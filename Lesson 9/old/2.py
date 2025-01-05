# У нас есть код с прошлого урока - движение квадрата на кнопки в окне.
# Сделаем по ООП парадигме. 

import pygame
import sys

def control(keys):
    returnValue = ''
    if keys[pygame.K_LEFT]: return 'LEFT'
    if keys[pygame.K_RIGHT]: return 'RIGHT'
    if keys[pygame.K_UP]: return 'UP'
    if keys[pygame.K_DOWN]: return 'DOWN'
    return returnValue

class Snake:
    def __init__(self):
        # Начальная позиция квадрата
        self._square_x, self._square_y = 100, 100
        self.color = (0,0,0)

    def mooving(self,action):

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
    

class Main:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()
        self.WINDOW_SIZE = (800, 600)
        # Создание окна
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        self.snake = Snake()

        self.background_color = (255,255,255)

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
            
            pygame.draw.rect(self.screen, self.snake.color, (*self.snake.getCoords(), 50, 50))
            
            pygame.display.flip() 

            # Ограничиваем скорость обновления до 60 FPS
            pygame.time.Clock().tick(60) 

if __name__ == '__main__':
    Main().gameLoop()
