import pygame


class Ball(object):

    def __init__(self):

        self.diam = 10
        self.surf = pygame.Surface((self.diam, self.diam))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.moveX = 3
        self.moveY = 3
