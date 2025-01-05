import pygame
import sys

#  В Pygame нет готовых кнопок в виде отдельных классов или компонентов. 
# Поэтому их либо нужно создавать самим, либо использовать что-то другое.
from button import Button

# Инициализация Pygame
pygame.init()

ORANGE = (255,128,0)
WHITE = (255,255,255)
GRAY = (128,128,128)
# Создание окна
screen = pygame.display.set_mode((800, 600))
button = Button(100, 300, 200, 50, "Нажми на меня",ORANGE,GRAY)


# Цикл игры
while True: 
    for event in pygame.event.get(): # получаем действия от игрока
        if event.type == pygame.QUIT: # если был нажат крестик 
            pygame.quit() # выйти из библиотеки
            sys.exit() # завершить работу программы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                print("Кнопка нажата!")
    
    mouse_position = pygame.mouse.get_pos()
    screen.fill(WHITE)
    button.draw(screen,mouse_position)
    
    # Обновление дисплея
    pygame.display.flip() # Эта функция обновляет весь экран, перерисовывая все элементы на нем.

