import pygame
from pygame.locals import *
from random import randint

pygame.init()

size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(size)
run = True
obstacles = []
clock = pygame.time.Clock()
FPS = 60

class Obstacle:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.width = 20
        self.create_obstacle()
        self.vel_x = -4
        self.rect1 = None
        self.rect2 = None

    def create_obstacle(self):
        top_height = randint(160, screen_height-10)
        self.top = [screen_width, 0, self.width, top_height-150]
        self.bottom = [screen_width, top_height, self.width, screen_height-top_height]

    def draw(self):
        self.rect1 = pygame.draw.rect(screen, (255, 255, 255), self.top)
        self.rect2 = pygame.draw.rect(screen, (255, 255, 255), self.bottom)
        self.top[0] += self.vel_x
        self.bottom[0] += self.vel_x

class Player:
    def __init__(self):
        img = pygame.image.load("bird.png")
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = screen_width/2
        self.vel_y = 0
        self.rad = 10
        self.acc = 0.3

    def draw(self):
        # self.rect = pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.rad)
        screen.blit(self.image, self.rect)
        self.check_collision()
        self.rect.y += self.vel_y
        self.vel_y += self.acc
        if self.vel_y < 10:
            self.vel_y += self.acc
        else:
            self.vel_y = 10

    def jump(self):
        self.vel_y = -10

    def check_collision(self):
        global run
        if self.rect.y < 0 or self.rect.y > screen_height:
            run = False
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect1) or self.rect.colliderect(obstacle.rect2):
                run = False
                print("COLLISION")
        


player = Player()
obstacles.append(Obstacle())
counter = 0

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
        if event.type == MOUSEBUTTONDOWN:
            player.jump()

    if counter == 100:
        obstacles.append(Obstacle())
        counter = 0
    counter +=1

    screen.fill((51,255,255))
    for obstacle in obstacles:
        obstacle.draw()

    player.draw()
    pygame.display.update()

pygame.quit()

