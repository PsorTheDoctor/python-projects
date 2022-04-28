import pygame
import numpy as np
import sys
import math

from text import Text
from button import Button

width = 600
height = 400
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Robot simulation')
pygame.display.set_mode((width, height))

window = pygame.display.get_surface()
clock = pygame.time.Clock()
fps = 24

angle = 0
object_pos = [width//2, height//2]
scale = 600
dist = 5
speed = 0.01

cube = np.zeros((8, 3, 1))
cube[0] = [[-1], [-1], [1]]
cube[1] = [[1], [-1], [1]]
cube[2] = [[1], [1], [1]]
cube[3] = [[-1], [1], [1]]
cube[4] = [[-1], [-1], [-1]]
cube[5] = [[1], [-1], [-1]]
cube[6] = [[1], [1], [-1]]
cube[7] = [[-1], [1], [-1]]

scale_txt = Text(10, 10, 100, 30)
scale_down_btn = Button(10, 40, 50, 30, '-')
scale_up_btn = Button(60, 40, 50, 30, '+')

dist_txt = Text(10, 90, 100, 40)
dist_down_btn = Button(10, 120, 50, 30, '-')
dist_up_btn = Button(60, 120, 50, 30, '+')

speed_txt = Text(10, 150, 100, 40)
speed_down_btn = Button(10, 180, 50, 30, '-')
speed_up_btn = Button(60, 180, 50, 30, '+')

while True:
    clock.tick(fps)
    window.fill(black)

    scale_txt.draw(window, 'Scale: ' + str(scale))
    scale_down_btn.draw(window)
    scale_up_btn.draw(window)

    dist_txt.draw(window, 'Distance: ' + str(dist))
    dist_down_btn.draw(window)
    dist_up_btn.draw(window)

    speed_txt.draw(window, 'Speed: ' + str(speed))
    speed_down_btn.draw(window)
    speed_up_btn.draw(window)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle += speed
            elif event.key == pygame.K_RIGHT:
                angle -= speed
            elif event.key == pygame.K_ESCAPE:
                sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if scale_down_btn.on_hover():
                scale -= 10
            elif scale_up_btn.on_hover():
                scale += 10
            elif dist_down_btn.on_hover():
                dist -= 1
            elif dist_up_btn.on_hover():
                dist += 1
            elif speed_down_btn.on_hover():
                if speed > 0.01:
                    speed -= 0.01
            elif speed_up_btn.on_hover():
                speed += 0.01

        if event.type == pygame.QUIT:
            sys.exit(0)

    idx = 0
    projected_points = np.zeros((cube.size, 2))

    rot_x = np.array([[1, 0, 0],
                      [0, math.cos(angle), -math.sin(angle)],
                      [0, math.sin(angle), math.cos(angle)]])

    rot_y = np.array([[math.cos(angle), 0, -math.sin(angle)],
                      [0, 1, 0],
                      [math.sin(angle), 0, math.cos(angle)]])

    rot_z = np.array([[math.cos(angle), -math.sin(angle), 0],
                      [math.sin(angle), math.cos(angle), 0],
                      [0, 0, 1]])

    for point in cube:
        rot_2d = rot_y.dot(point)
        rot_2d = rot_x.dot(rot_2d)
        rot_2d = rot_z.dot(rot_2d)

        z = 1 / (dist - rot_2d[2][0])
        projection_mat = np.array([[z, 0, 0],
                                   [0, z, 0]])

        projected_2d = projection_mat.dot(rot_2d)

        x = int(projected_2d[0][0] * scale) + object_pos[0]
        y = int(projected_2d[1][0] * scale) + object_pos[0]

        projected_points[idx] = [x, y]
        pygame.draw.circle(window, white, (x, y), 5)
        idx += 1

    # angle += speed
    pygame.display.update()
