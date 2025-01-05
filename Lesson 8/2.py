# Теперь заставим созданный квадрат двигаться нажимая на клавиши. 
# По истечению времени цвета объектов будут меняться

import pygame
import sys

from random import randint

def random_color() -> tuple: 
    return (randint(0,255),randint(0,255),randint(0,255))



# Инициализация Pygame
pygame.init()
WINDOW_SIZE = (800, 600)
# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)

# Начальная позиция квадрата
square_x, square_y = 100, 100

background_color = (255,255,255)
rect_color = (0,0,0)

timer=0

# Цикл игры
while True: 
    timer+=1
    for event in pygame.event.get(): # получаем действия от игрока
        if event.type == pygame.QUIT: # если был нажат крестик 
            pygame.quit() # выйти из библиотеки
            sys.exit() # завершить работу программы
    
    keys = pygame.key.get_pressed() # Получаем состояние всех клавиш
    
    # Обновляем позицию квадрата. Движение по координатам.
    if keys[pygame.K_LEFT] and square_x > 0:
        square_x -= 5 
    if keys[pygame.K_RIGHT] and square_x < 750: 
        # WINDOW_SIZE[0] = 800, 800 - 50 (ширина квадрата) = 750. 
        # Таким образом мы не выходим за границы экрана.
        square_x += 5
    if keys[pygame.K_UP] and square_y > 0:
        square_y -= 5
    if keys[pygame.K_DOWN] and square_y < 550:
        square_y += 5
    if timer>100:
        timer = 0
        background_color=random_color()  
        rect_color=random_color()
    
    # Очистка экрана
    screen.fill(background_color) # fill - заполнить
    
    # Рисование
    # screen - поле где будем отрисовывать объект, далее (255, 0, 0) это параметры rgb - цвет
    # можно посмотреть на любом сайте в браузере
    # далее  (x, y, width, height) - первые два числа расположение объекта по координатам
    # последние два - размер соответственно
    pygame.draw.rect(screen, rect_color, (square_x, square_y, 50, 50))
    
    # Обновление дисплея
    pygame.display.flip() # Эта функция обновляет весь экран, перерисовывая все элементы на нем.

    # Ограничиваем скорость обновления до 60 FPS
    pygame.time.Clock().tick(60) # чем выше - тем больше скорость. 
    # Если кто-то из вас играл в игры от компании Bethesda - знают, что чем выше фпс, тем быстрее
    # игровой процесс. Так можно менять значение фпс чтобы быстрее загружаться между локациями.
