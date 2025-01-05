import pygame
import sys

import backend.consts as const
from backend.objects.field import Field
from backend.objects.snake import Snake
from backend.objects.fruit import Fruit
from backend.control import Control
from view import View

class Main:
    def __init__(self):
        
        pygame.init()
        self.WINDOW_SIZE = const.WINDOW_SIZE
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.view = View(self.screen)
        self.snake = Snake()
        self.gameField = Field(400,760,40,40)
        self.fruit = Fruit ()
        self.gameScore = 0 # домашняя работа
        self.control = Control(self.view,self.snake,self.fruit,self.gameField,self.gameScore)

    def gameLoop(self):
        game = True
        while game: 
            for event in pygame.event.get(): # получаем действия от игрока
                if event.type == pygame.QUIT: # если был нажат крестик 
                    pygame.quit() # выйти из библиотеки
                    sys.exit() # завершить работу программы
 
            game=self.control.backProcess()
            self.control.frontProcess()
            pygame.display.flip() 
            pygame.time.Clock().tick(7)

if __name__ == '__main__':
    Main().gameLoop()
