import pygame


class Paddle(object):

    def __init__(self):

        self.width = 100
        self.height = 10
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0, 150, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 350
        self.rect.y = 550
        self.moveX = 0
