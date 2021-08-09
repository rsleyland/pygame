import sys, pygame
from random import randint
from pygame.locals import MOUSEBUTTONDOWN, KEYDOWN
pygame.init()

size = width, height = 480, 480
speed = [10, 5]
black = 0, 0, 0
white = 255, 255, 255
grey = 100, 100, 100
red = 255, 0, 0
ballx = width/2
bally = height/2

screen = pygame.display.set_mode(size)

tiles = [(0,0) for i in range(400)] #tile size is 24x24
for y in range(20):
    for x in range(20):
        tiles[(y*20)+x] = (x*24,y*24, (randint(0,255),randint(0,255),randint(0,255)))

for tile in tiles:
    print(tile)

#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()

directions = {pygame.K_LEFT: 'Left', pygame.K_UP: 'Up', pygame.K_RIGHT: 'Right', pygame.K_DOWN: 'Down'}    # Left Up Right Down 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == MOUSEBUTTONDOWN:
        #     newpos = pygame.mouse.get_pos()
        #     ballrect.center = newpos
        if event.type == KEYDOWN:
            if event.key in directions.keys():
                print("DIRECTIONAL KEY PRESSED", directions[event.key])


    screen.fill(white)

    for i, tile in enumerate(tiles):
        tiles[i] = pygame.draw.rect(surface=screen, color=tile[2], rect=(tile[0],tile[1],24, 24), width=0, border_radius=0)

    ball = pygame.draw.circle(screen, black, (ballx,bally), 10)
    ballx += speed[0]
    bally += speed[1]

    if ballx < 0 or ballx > width:
        speed[0] = -speed[0]
        if ballx <= 0:
            ballx = 0
        else:
            ballx = width
    if bally < 0 or bally > height:
        speed[1] = -speed[1]
        if bally <= 0:
            bally = 0
        else:
            bally = height

    
    for i, tile in enumerate(tiles):
        if ball.colliderect(tile):
            #tiles[i] = (tile[0], tile[1], red)
            tile = pygame.draw.rect(surface=screen, color=red, rect=(tile[0],tile[1],24, 24), width=0, border_radius=0)

    ball = pygame.draw.circle(screen, black, (ballx,bally), 10)

    pygame.display.flip()