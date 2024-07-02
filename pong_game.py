# Description: Remake Pong game

import pygame

# Initializes the window
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')

run = True

clock = pygame.time.Clock()

# Allows game to run
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
 

    






    pygame.display.update()

    clock.tick(30)

pygame.quit()