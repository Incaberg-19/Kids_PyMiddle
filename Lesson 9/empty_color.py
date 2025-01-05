import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Пустой прямоугольник с обводкой")


rect = pygame.Rect(100, 100, 200, 200)
EMPTY_COLOR = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисование пустого прямоугольника с обводкой
    width_borders = 2
    pygame.draw.rect(screen, EMPTY_COLOR, rect, width_borders)
    # 

    # Обновление экрана
    pygame.display.flip()
