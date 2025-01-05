# У нас есть код с прошлого урока - движение квадрата на кнопки в окне.
# Сделаем по ООП парадигме. 

import pygame
import sys

class Main:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()
        self.WINDOW_SIZE = (800, 600)
        # Создание окна
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        # Начальная позиция квадрата
        self.square_x, self.square_y = 100, 100

        self.background_color = (255,255,255)
        self.rect_color = (0,0,0)

    def gameLoop(self):

        # Цикл игры
        while True: 
            for event in pygame.event.get(): # получаем действия от игрока
                if event.type == pygame.QUIT: # если был нажат крестик 
                    pygame.quit() # выйти из библиотеки
                    sys.exit() # завершить работу программы
            
    
            # Обновляем позицию квадрата. Движение по координатам.
            self.mooving()
        
            self.screen.fill(self.background_color) 
            
            pygame.draw.rect(self.screen, self.rect_color, (self.square_x, self.square_y, 50, 50))
            
            pygame.display.flip() 

            # Ограничиваем скорость обновления до 60 FPS
            pygame.time.Clock().tick(60) 

    def mooving(self):
        keys = pygame.key.get_pressed() # Получаем состояние всех клавиш
        # Обновляем позицию квадрата. Движение по координатам.
        if keys[pygame.K_LEFT] and self.square_x > 0:
            self.square_x -= 5 
        if keys[pygame.K_RIGHT] and self.square_x < 750: # WINDOW_SIZE[0] = 800, 800 - 50 (ширина квадрата) = 750
            self.square_x += 5
        if keys[pygame.K_UP] and self.square_y > 0:
            self.square_y -= 5
        if keys[pygame.K_DOWN] and self.square_y < 550:
            self.square_y += 5

if __name__ == '__main__':
    Main().gameLoop()
