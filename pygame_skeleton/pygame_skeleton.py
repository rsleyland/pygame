import pygame
from pygame.locals import *

pygame.init()

size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    
    screen.fill(BLACK)  #fill black

    pygame.display.update()

pygame.quit()