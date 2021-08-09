import pygame
from pygame.locals import *

pygame.init()

size = screen_width, screen_height = 600, 600
screen = pygame.display.set_mode(size)
run = True


class Arrow:
    def __init__(self) -> None:
        self.image = pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load("arrow.png"), (100, 50)), 0, 1)
        self.rect = self.image.get_rect()
        

    def draw(self, vec):
        
        temp = pygame.transform.rotate(self.image, vec.vec.angle_to(pygame.math.Vector2(0,0)))
        self.rect.midbottom = vec.pos
        self.rect.midtop = (vec.pos[0]+(100*vec.vec[0]), vec.pos[1]+(100*vec.vec[1]))
        screen.blit(temp, self.rect)

class Vector_line:
    def __init__(self) -> None:
        self.vec = pygame.math.Vector2(0,-1)
        self.pos = (200,200)
        self.dir = None
        self.turning = False

    def draw(self):
        if self.turning:
            self.rotate()
        pygame.draw.line(screen, (0,0,0), start_pos=self.pos, end_pos=(self.pos[0]+(100*self.vec[0]), self.pos[1]+(100*self.vec[1])), width=3)

    def rotate(self):
        if self.dir == "R":
            self.vec = self.vec.rotate(2)
        elif self.dir == "L":
            self.vec = self.vec.rotate(-2)

vec = Vector_line()
arr = Arrow()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_LEFT:
                vec.turning = True
                vec.dir = "L"
            if event.key == K_RIGHT:
                vec.turning = True
                vec.dir = "R"
        if event.type == KEYUP:
             if event.key == K_LEFT or event.key == K_RIGHT:
                vec.turning = False
    
    screen.fill((255,255,255))
    vec.draw()
    arr.draw(vec)
    pygame.display.update()

pygame.quit()