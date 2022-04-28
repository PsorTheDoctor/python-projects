import pygame


class Text:
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, updated_text=''):
        if updated_text != '':
            font = pygame.font.SysFont('verdana', 12)
            text = font.render(updated_text, True, (255, 255, 255))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))
        elif self.text != '':
            font = pygame.font.SysFont('verdana', 12)
            text = font.render(self.text, True, (255, 255, 255))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))
