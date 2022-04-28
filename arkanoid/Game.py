import pygame
import sys

from Arkanoid_v1.Paddle import Paddle
from Arkanoid_v1.Ball import Ball
from Arkanoid_v1.Block import Block
from Arkanoid_v1.Score import Score


class Game(object):

    def __init__(self):
        pygame.init()

        self.width = 600
        self.height = 800
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Arkanoid')
        screen = pygame.display.get_surface()

        ball = Ball()
        paddle = Paddle()
        block_list = []
        block_cols = 6
        score = Score(block_cols)

        x = 5
        y = 5
        for i in range(block_cols):
            block = Block(x, y)
            block_list.append(block)
            x += 100

        pygame.display.flip()
        fps = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        paddle.moveX = -5
                    elif event.key == pygame.K_RIGHT:
                        paddle.moveX = 5
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                elif event.type == pygame.KEYUP:
                    paddle.moveX = 0
                elif event.type == pygame.QUIT:
                    sys.exit(0)

            screen.fill((0, 0, 0))

            if paddle.rect.colliderect(ball):
                ball.moveY = 3

            for i in range(block_cols):
                if block_list[i].rect.colliderect(ball):
                    ball.moveY = -3
                    block_list[i].exists = False
                    score.counter += score.per_block
                if block_list[i].exists:
                    screen.blit(block_list[i].surf, block_list[i])

            paddle.rect.x += paddle.moveX
            if paddle.rect.x < 0:
                paddle.rect.x = 0
            elif paddle.rect.x > self.width - paddle.width:
                paddle.rect.x = self.width - paddle.width

            screen.blit(paddle.surf, paddle)

            ball.rect.x -= ball.moveX
            if ball.rect.x < 0 or ball.rect.x > self.width - ball.diam:
                ball.moveX *= -1

            ball.rect.y -= ball.moveY
            if ball.rect.y < 0:
                ball.moveY *= -1

            screen.blit(ball.surf, ball)

            score.count(screen)

            if score.counter == score.max:
                screen.fill((0, 0, 0))
                score.notify("You Won!", screen)
            elif ball.rect.y > self.height:
                screen.fill((0, 0, 0))
                score.notify("Game Over!", screen)

            pygame.display.update()
            fps.tick(60)


if __name__ == '__main__':
    Game()
