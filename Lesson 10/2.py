import pygame
import sys

#  В Pygame нет готовых кнопок в виде отдельных классов или компонентов. 
# Поэтому их либо нужно создавать самим, либо использовать что-то другое.
from button import Button

pygame.mixer.init() # инизиализация модуля работы со звуками

# Инициализация Pygame
pygame.init()

ORANGE = (255,128,0)
WHITE = (255,255,255)
GRAY = (128,128,128)
# Создание окна
screen = pygame.display.set_mode((800, 600))
button = Button(100, 300, 200, 50, "Нажми на меня",ORANGE,GRAY)
button2 = Button(500, 300, 200, 50, "Нажми на меня",ORANGE,GRAY)
button3 = Button(500, 500, 200, 50, "Нажми на меня",ORANGE,GRAY)
button4 = Button(100, 500, 200, 50, "Нажми на меня",ORANGE,GRAY)

#Для постоянного воспроизведения музыки лучше использовать music,
# а для коротких звуковых эффектов - Sound().

pygame.mixer.music.load('phonk.mp3')
# pygame.mixer.music.load('sound1.wav') # пример чтобы показать зацикливание
pygame.mixer.music.play(-1) # -1 зациклить
'''
фоновая музыка: pygame.mixer.music.load().
Функция не возвращает никакого "музыкального" объекта, поэтому результат ее вызова не присваивается переменной.
С помощью функции music.play() файл начинает проигрываться. Если требуется зациклить композицию, то в play()
передается число -1. Положительный аргумент указывает на количество повторов + одно дополнительное.
То есть, если надо проиграть композицию 2 раза, то в функцию передается число 1.
'''
# Установка громкости
volume = 0.1  # Громкость от 0.0 (мут) до 1.0 (максимальная громкость)
pygame.mixer.music.set_volume(volume)

sound = pygame.mixer.Sound('sound1.wav')

# Цикл игры
while True: 
    for event in pygame.event.get(): # получаем действия от игрока
        if event.type == pygame.QUIT: # если был нажат крестик 
            pygame.quit() # выйти из библиотеки
            sys.exit() # завершить работу программы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                # print("Кнопка нажата!")
                # скачивать отсюда - mixkit.co/free-sound-effects/game/
                sound.play()
            if button2.is_clicked(event.pos):
                # sound.pause() # 'pygame.mixer.Sound' object has no attribute 'pause'
                sound.stop()
            
            if button3.is_clicked(event.pos):
                pygame.mixer.music.pause()

            if button4.is_clicked(event.pos):
                pygame.mixer.music.unpause()


    
    mouse_position = pygame.mouse.get_pos()
    screen.fill(WHITE)
    button.draw(screen,mouse_position)
    button2.draw(screen,mouse_position)
    button3.draw(screen,mouse_position)
    button4.draw(screen,mouse_position)
    
    # Обновление дисплея
    pygame.display.flip() # Эта функция обновляет весь экран, перерисовывая все элементы на нем.

