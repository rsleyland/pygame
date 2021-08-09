import pygame
from pygame.locals import *
import json

pygame.init()
size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
WHITE = 255, 255, 255
RED = 255, 0, 0
run = True
data = {}

gaps = 4
size = width, height = 28, 28


sprite_sheet = pygame.image.load("BG8.png").convert()
ss_rect = sprite_sheet.get_rect()

# width = 512  - 16 boxes so 32 width and 32 height
# height = 867 - 22 boxes = 704 so 163 space

count = 1
name = "sprite"

for row in range(22):
    for col in range(16):
        data[f"sprite{count}"] = {
            'x' : col*32,
            'y' : row*32,
            'w' : 32,
            'h' : 32
        }
        count +=1

with open("BG8.json", 'w') as f:
    json.dump(data, f, indent=4)


class Grid:

    def __init__(self) -> None:
        pass

    def draw(self):
        for row in range(23):
            for col in range(17):
                pygame.draw.line(screen, RED, start_pos=(col*32, 0), end_pos=(col*32, 704), width=1)
            pygame.draw.line(screen, RED, start_pos=(0, row*32), end_pos=(512, row*32), width=1)

grids = Grid()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    
    screen.fill(WHITE)

    screen.blit(sprite_sheet, (0,0))
    grids.draw()
    pygame.display.update()

pygame.quit()