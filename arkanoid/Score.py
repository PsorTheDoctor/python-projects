import pygame


class Score(object):

    def __init__(self, num_of_blocks):

        self.counter = 0
        self.per_block = 10
        self.max = num_of_blocks * self.per_block

    def count(self, screen):
        font = pygame.font.SysFont('verdana', 20)
        text = font.render('Score: ' + str(self.counter), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (500, 670)
        screen.blit(text, text_rect)

    @staticmethod
    def notify(comment, screen):
        font = pygame.font.SysFont('verdana', 60)
        text = font.render(comment, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (300, 300)
        screen.blit(text, text_rect)
