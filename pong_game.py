# Description: Remake Pong game

import pygame as pg

# Initializes the window
pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Pong')

# Position & Size Variables
player_right_x = 765
player_right_y = 250
player_left_x = 35
player_left_y = 250
width = 5
height = 65
circle_x = 400
circle_y = 300
radius = 5

run = True

clock = pg.time.Clock()

# Allows game to run
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT: 
            run = False
    
    player_left = pg.draw.rect(screen, (255, 255, 255), [player_left_x, player_left_y, width, height])
    player_right = pg.draw.rect(screen, (255, 255, 255), [player_right_x, player_right_y, width, height])
    ball = pg.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), radius)
    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            player_left_y -= 10
        if event.key == pg.K_DOWN:
            player_left_y += 10
        if event.key == pg.K_w:
            player_right_y -= 10



    pg.display.update()

    clock.tick(30)

pg.quit()