import pygame


class Button:
    def __init__(self, x, y, width, height, text,color,current_color):
        self.current_color = current_color
        self.color = color
        self.rect = pygame.Rect(x, y, width, height) # создали квадрат предполагающий кнопку
        self.text = text # сохранили переданный текст
        self.font = pygame.font.Font(None, 36) # усnановили шрифт
        # создали область куда запишем текст (в саму кнопку нельзя записать)
        self.text_surface = self.font.render(self.text, True, (50, 50, 50)) 

    def draw(self, screen,mouse_pos):

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.current_color, self.rect) 
        else:
            pygame.draw.rect(screen, self.color, self.rect) 
            
        screen.blit(self.text_surface, (self.rect.x + 10, self.rect.y + 10))
        # отрисовали отдельный элемент text_surface при помощи .blit

    def is_clicked(self, mouse_pos):
        # collidepoint проверяет, находится ли точка mouse_pos внутри прямоугольника self.rect
        return self.rect.collidepoint(mouse_pos)
    
