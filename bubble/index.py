import pygame
from pygame.locals import *
from random import randint
import math
pygame.init()

size = screen_width, screen_height = 600, 600
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0
WHITE = 255, 255, 255
run = True
bubbles = []

colours = {
    1 : (255, 0 , 0), #RED
    2 : (0, 0 , 255),  #BLUE
    3 : (0, 255 , 0), #GREEN
    4 : (255, 128 , 0), #ORANGE
    5 : (255, 0 , 255), #PINK
    6 : (255, 255 , 0), #YELLOW
}



def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

class Arrow:
    def __init__(self) -> None:
        self.img = pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load("img/arrow.png").convert(), (150,50)), -90, 1)
        self.rect = self.img.get_rect()
        self.rect.midbottom = (screen_width//2, screen_height+5)
        self.pivot = self.rect.midbottom
        self.offset = pygame.math.Vector2(0, -50)
        self.angle = 0
        self.rotating = False
        self.dir = None
        self.fire_pos = self.rect.midtop

    def draw(self):
        rotated_image, rect = rotate(self.img, self.angle, self.pivot, self.offset)
        self.fire_pos = rect.midtop
        screen.blit(rotated_image, rect)
        if self.rotating:
            self.rotate(self.dir)

    def rotate(self, dir):
        if dir == "L":
            if self.angle > -75:
                self.angle -= 2
        if dir == "R":
            if self.angle < 75:
                self.angle += 2


class Vect:
    def __init__(self) -> None:
        self.vec = pygame.math.Vector2(0,-1)
        self.pos = (screen_width//2,screen_height)
        self.dir = None
        self.turning = False
        self.angle = 0

    def draw(self):
        if self.turning:
            self.rotate()
        #pygame.draw.line(screen, (255,255,255), start_pos=self.pos, end_pos=(self.pos[0]+(120*self.vec[0]), self.pos[1]+(120*self.vec[1])), width=3)

    def rotate(self):
        
        if self.dir == "L":
            if self.angle > -75:
                self.angle -= 2
                self.vec = self.vec.rotate(-2)
        elif self.dir == "R":
            if self.angle < 75:
                self.angle += 2
                self.vec = self.vec.rotate(2)

    
        

class Bubble:

    def __init__(self, vect) -> None:
        self.pos = (vect.pos[0]+(120*vect.vec[0]), vect.pos[1]+(120*vect.vec[1]))
        self.vel = 10
        self.vec = vect.vec
        self.fired = False
        self.finished = False
        self.colour = colours[randint(1,6)]
        self.circ = None
        
    def draw(self, vect):
        if self.fired:
            if self.check_collision(vect):
                self.pos = (self.pos[0]+(self.vel*self.vec[0]), self.pos[1]+(self.vel*self.vec[1]))
                self.checkonscreen(vect)
        elif not self.finished:
            self.pos = (vect.pos[0]+(130*vect.vec[0]), vect.pos[1]+(130*vect.vec[1]))
        
        self.circ = pygame.draw.circle(screen, self.colour, self.pos, 10)
        
    def fire(self, vect):
        self.fired = True
        self.vec = vect.vec
        

    def checkonscreen(self, vect):
        if self.pos[0]<= 10 or self.pos[0] > screen_width-10 or self.pos[1] <=10:
            self.fired = False
            self.finished = True
            temp = Bubble(vect)
            bubbles.append(temp)
            

    def check_collision(self, vect):
        temp = (self.pos[0]+(self.vel*self.vec[0]), self.pos[1]+(self.vel*self.vec[1]))
        for bub in bubbles:
            dist = math.sqrt(math.pow((bub.pos[0]-temp[0]),2)+math.pow((bub.pos[1]-temp[1]),2))
            if self != bub and dist < 20:
                print("COLLISION")
                self.finished = True
                self.fired = False
                temp = Bubble(vect)
                bubbles.append(temp)
                return False
        return True

arr = Arrow()
vect = Vect()
bub = Bubble(vect)
bubbles.append(bub)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_LEFT:
                arr.dir = "L"
                vect.dir = "L"
                arr.rotating = True
                vect.turning = True
            if event.key == K_RIGHT:
                arr.dir = "R"
                vect.dir = "R"
                arr.rotating = True
                vect.turning = True
            if event.key == K_SPACE:
                bub.fire(vect)
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                arr.rotating = False
                vect.turning = False

    screen.fill(WHITE)
    arr.draw()
    for bub in bubbles:
        bub.draw(vect)
    vect.draw()
    pygame.display.update()

pygame.quit()
