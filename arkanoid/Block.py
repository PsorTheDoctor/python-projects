import pygame


class Block(object):

    def __init__(self, x, y):

        self.width = 90
        self.height = 45
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0, 204, 153))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.exists = True
