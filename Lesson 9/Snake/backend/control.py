from pygame import key
from pygame.locals import *
from .consts import *

# проверка вхождения одного списка в другой
def check_unification(list1,list2):
    for element in list1:
        if element in list2:
            return True
    else:
        return False

class Control:
    def __init__(self,view,snake,fruit,gameField,gameScore): # gameScore - домашняя работа
        self.gameScore=gameScore # домашняя работа
        self.view=view
        self.snake=snake
        self.fruit = fruit
        self.gameField = gameField
        self.returnValue = True

    def backProcess(self):

        keys = key.get_pressed() 
        action = None

        if keys[K_LEFT]: action = 'LEFT'
        if keys[K_RIGHT]: action = 'RIGHT'
        if keys[K_UP]: action = 'UP'
        if keys[K_DOWN]: action = 'DOWN'

        self.snake.setDirection(action)
        self.snake.moving()

        if check_unification([self.fruit.getRect()],self.snake.getListRects())==True:
            self.fruit.changePosition()
            self.snake.grow()
            self.gameScore+=1 # домашняя работа

        self.returnValue = self.checkBorders()

        return self.returnValue

    def frontProcess(self):
        self.view.screen.fill(DARK) 
        self.view.printRectList(self.gameField.getListRects(), WHITE,1)
        self.view.printRectList([self.fruit.getRect()],self.fruit.color)
        self.view.printRectList(self.snake.getListRects(),self.snake.color)
        # реализация домашней работы
        if self.returnValue==False:
            self.view.printLoseWindow(self.gameScore)

    def checkBorders(self):
        returnValue=True
        for rect in self.snake.getListRects():
            if ((rect.x+RECT_SIZE) > WINDOW_SIZE[0]) or rect.x < 0:
                returnValue = False
            elif ((rect.y+RECT_SIZE) > WINDOW_SIZE[1]) or rect.y < 0:
                returnValue = False
        return returnValue


