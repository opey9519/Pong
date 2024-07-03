# Description: Remake Pong game

import pygame as pg
import random

# Initializes the window
pg.init()

HEIGHT = 600
WIDTH = 800
FONT = pg.font.SysFont('Consolas', int(WIDTH/20))

screen = pg.display.set_mode((WIDTH, HEIGHT))
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
rand_x = random.choice([-8, 8])
rand_y = random.randint(-10, 10)

player_score, CPU_score = 0, 0

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

    # Automatic movement for the CPU player
    CPU_y += CPU_change
    if CPU_y == 550 or CPU_y == 40:
        CPU_change *= -1
    
    circle_x -= rand_x
    circle_y -= rand_y

    # Ball and Screen collision logic
    if circle_y >= HEIGHT:
        rand_y *= -1
    if circle_y <= 0:
        rand_y *= -1
    if circle_x <= 0:
        CPU_score += 1
        circle_x, circle_y = (WIDTH/2, HEIGHT/2)
        rand_x = random.choice([-8, 8])
        rand_y = random.randint(-10, 10)
    if circle_x >= WIDTH:
        player_score += 1
        circle_x, circle_y = (WIDTH/2, HEIGHT/2)
        rand_x = random.choice([-8, 8])
        rand_y = random.randint(-10, 10)

    screen.fill([0,0,0])

    player = pg.draw.rect(screen, (255, 255, 255), [player_x, player_y, width, height])
    CPU = pg.draw.rect(screen, (255, 255, 255), [CPU_x, CPU_y, width, height])
    ball = pg.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), radius)

    # Ball and Player + CPU collision logic
    if player_x - radius <= circle_x <= player_x and circle_y in range(player.top - ball.width, player.bottom + ball.width):
        rand_x *= -1
    if CPU_x - radius <= circle_x <= CPU_x and circle_y in range(CPU.top - ball.width, CPU.bottom + ball.width):
        rand_x *= -1

    # Creating score objects
    player_score_text = FONT.render(str(player_score), True, 'white')
    CPU_score_text = FONT.render(str(CPU_score), True, 'white')

    # Putting score objects on screen
    screen.blit(player_score_text, (WIDTH/2+50, 50))
    screen.blit(CPU_score_text, (WIDTH/2-50, 50))

    pg.display.update()

    clock.tick(30)

pg.quit()