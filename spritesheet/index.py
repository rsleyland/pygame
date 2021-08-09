import pygame
from pygame.locals import *
from spritesheet2 import Spritesheet

pygame.init()
size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
WHITE = 255, 255, 255
run = True
trainer_count = 0
sprite_count = 0

my_spritesheet = Spritesheet("BG8.png")
# trainer = [
#     my_spritesheet.parse_sprite("trainer1"),
#     my_spritesheet.parse_sprite("trainer2"),
#     my_spritesheet.parse_sprite("trainer3"),
#     my_spritesheet.parse_sprite("trainer4"),
#     my_spritesheet.parse_sprite("trainer5")
# ]
# f_trainer = [
#     my_spritesheet.parse_sprite("f_trainer1"),
#     my_spritesheet.parse_sprite("f_trainer2"),
#     my_spritesheet.parse_sprite("f_trainer3"),
#     my_spritesheet.parse_sprite("f_trainer4"),
#     my_spritesheet.parse_sprite("f_trainer5")
# ]

#352

sprites = [my_spritesheet.parse_sprite(f"sprite{x+1}") for x in range(352)]


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_SPACE:
                sprite_count += 1
                if sprite_count == 351:
                    sprite_count = 0
    
    screen.fill(WHITE)

    # screen.blit(trainer[trainer_count], (0,0))
    # screen.blit(f_trainer[trainer_count], (0,200))
    screen.blit(pygame.transform.scale(sprites[sprite_count], (50,50)), (200,200))

    pygame.display.update()

pygame.quit()