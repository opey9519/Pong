# Description: Remake Pong game

import pygame as pg
import random

# Initializes the window
pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Pong')

# Position & Size Variables
CPU_x = 765
CPU_y = 250
player_x = 35
player_y = 250
CPU_change = 10
width = 5
height = 75
circle_x = 400
circle_y = 300
radius = 5


run = True

clock = pg.time.Clock()

# Allows game to run
while run:
    screen.fill([0,0,0])
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            run = False
    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            player_y -= 10
        if event.key == pg.K_DOWN:
            player_y += 10

    CPU_y += CPU_change
    if CPU_y == 550 or CPU_y == 40:
        CPU_change *= -1
    
    screen.fill([0,0,0])

    player = pg.draw.rect(screen, (255, 255, 255), [player_x, player_y, width, height])
    CPU = pg.draw.rect(screen, (255, 255, 255), [CPU_x, CPU_y, width, height])
    ball = pg.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), radius)


    pg.display.update()

    clock.tick(40)

pg.quit()