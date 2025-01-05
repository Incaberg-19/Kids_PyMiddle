from pygame import draw
from tkinter import messagebox

class View:
    def __init__(self,screen):
        self.screen = screen

    def printRectList(self,rectList,color,width_borders = 0):
        for rect in rectList:
            draw.rect(self.screen, color, rect,width_borders)

    def printLoseWindow(self,gameScore):
        messagebox.showinfo("Упс! Вы проиграли!", f"Ваш итоговый счёт: {gameScore}")
