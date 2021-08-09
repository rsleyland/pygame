import pygame
from pygame.locals import *
from random import randint

pygame.init()
TRANSPARENT = 255, 0, 255

cherry_positions = [
    (30,30), (60,30), (90,30), (120,30), (150,30), (180,30), (240,30), (270,30), (300,30),
    (330,30), (390,30), (420,30), (450,30), (480,30), (510,30), (540,30),
    (30,540), (60,540), (90,540), (120,540), (150,540), (180,540), (240,540), (270,540), (300,540),
    (330,540), (390,540), (420,540), (450,540), (480,540), (510,540), (540,540),
    (30,30), (30,60), (30,90), (30,120), (30,150), (30,180), (30,210), (30,240), (30,270), (30,300),
    (30,330), (30,360), (30,390), (30,420), (30,450), (30,480), (30,510), (30,540),
    (540,30), (540,60), (540,90), (540,120), (540,150), (540,180), (540,210), (540,240), (540,270), (540,300),
    (540,330), (540,360), (540,390), (540,420), (540,450), (540,480), (540,510), (540,540)

]

#tl_corn = 1
#tr_corn = 2
#bl_corn = 3
#br_corn = 4
#straight_hori_t = 5
#straight_vert_l = 6
#straight_hori_b = 7
#straight_vert_r = 8

#SIZE - 20 x 20
game_map = [
    [1,5,5,5,5,5,5,9,5,5,5,5,9,5,5,5,5,5,5,2],
    [6,0,0,0,0,0,0,11,0,0,0,0,11,0,0,0,0,0,0,8],
    [6,0,1,5,5,2,0,11,0,1,2,0,11,0,1,5,5,2,0,8],
    [6,0,6,0,0,8,0,12,0,6,8,0,12,0,6,0,0,8,0,8],
    [6,0,3,7,7,4,0,0,0,3,4,0,0,0,3,7,7,4,0,8],
    [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,1,5,5,5,5,2,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,6,0,0,0,0,8,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,6,0,0,0,0,8,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,3,7,7,7,7,4,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [6,0,0,0,0,0,0,1,5,5,5,5,2,0,0,0,0,0,0,8],
    [6,0,1,5,5,2,0,6,0,0,0,0,8,0,1,5,5,2,0,8],
    [6,0,6,0,0,8,0,3,7,7,7,7,4,0,6,0,0,8,0,8],
    [6,0,6,0,0,8,0,0,0,0,0,0,0,0,6,0,0,8,0,8],
    [6,0,6,0,0,8,0,0,0,1,2,0,0,0,6,0,0,8,0,8],
    [6,0,6,0,0,8,0,13,0,6,8,0,13,0,6,0,0,8,0,8],
    [6,0,3,7,7,4,0,11,0,3,4,0,11,0,3,7,7,4,0,8],
    [6,0,0,0,0,0,0,11,0,0,0,0,11,0,0,0,0,0,0,8],
    [3,7,7,7,7,7,7,10,7,7,7,7,10,7,7,7,7,7,7,4]


]



class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
        self.sheet.set_colorkey(TRANSPARENT)

    def getImage(self, x, y, width, height):
        self.sheet.set_clip(pygame.Rect(x, y, width, height))
        return self.sheet.subsurface(self.sheet.get_clip())


size = screen_width, screen_height = 600, 600
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
run = True
FPS = 20
clock = pygame.time.Clock()
spritesheet = Spritesheet("img/spritesheet.png")
spritesheet2 = Spritesheet("img/spritesheet2.png")
tiles = []


#SPRITES
#tl_corn = 1
#tr_corn = 2
#bl_corn = 3
#br_corn = 4
#straight_hori_t = 5
#straight_vert_l = 6
#straight_hori_b = 7
#straight_vert_r = 8

left_pman = spritesheet.getImage(0,0,30,30)
right_pman = spritesheet.getImage(32,0,30,30)
down_pman = spritesheet.getImage(64,0,30,30)
up_pman = spritesheet.getImage(96,0,30,30)

tl_corner = pygame.transform.scale(spritesheet2.getImage(320,0,10,10), (30, 30))
tr_corner = pygame.transform.flip(tl_corner, 1, 0)
bl_corner = pygame.transform.flip(tl_corner, 0, 1)
br_corner = pygame.transform.flip(tl_corner, 1, 1)
straight_hori_left = pygame.transform.scale(spritesheet2.getImage(340,0,10,10), (30, 30))
straight_vert_top = pygame.transform.scale(spritesheet2.getImage(320,10,10,10), (30, 30))
straight_hori_right = pygame.transform.flip(straight_hori_left, 0, 1)
straight_vert_bot = pygame.transform.flip(straight_vert_top, 1, 0)
t_junc_top = pygame.transform.flip(pygame.transform.scale(pygame.image.load("img/t_junc.png"), (30,30)), 0, 1)
t_junc_bot = pygame.transform.flip(t_junc_top, 0, 1)
straight_wide = pygame.transform.scale(pygame.image.load("img/wide_straight.png"), (30,30))
end_wide_bot = pygame.transform.flip(pygame.transform.scale(pygame.image.load("img/wide_end.png"), (30,30)), 0, 1)
end_wide_top = pygame.transform.flip(end_wide_bot, 0, 1)


assets = {
    1 : tl_corner,
    2: tr_corner,
    3: bl_corner,
    4: br_corner,
    5: straight_hori_left,
    6: straight_vert_top,
    7: straight_hori_right,
    8: straight_vert_bot,
    9: t_junc_top,
    10: t_junc_bot,
    11: straight_wide,
    12: end_wide_bot,
    13: end_wide_top
}

class Player:

    def __init__(self) -> None:
        self.img = pygame.transform.scale(right_pman, (25,25))
        self.rect = self.img.get_rect()
        self.rect.x = 120
        self.rect.y = 150
        self.dir = "RIGHT"
        self.vel_x = 1
        self.vel_y = 0


    def draw(self):
        screen.blit(self.img, self.rect)
        self.move()

    def move(self):
        if self.dir == "RIGHT":
            self.vel_x = 15
            self.vel_y = 0
            self.img = right_pman
        elif self.dir == "LEFT":
            self.vel_x = -15
            self.vel_y = 0
            self.img = left_pman
        elif self.dir == "UP":
            self.vel_x = 0
            self.vel_y = -15
            self.img = up_pman
        elif self.dir == "DOWN":
            self.vel_x = 0
            self.vel_y = 15
            self.img = down_pman
        self.rect.x, self.rect.y = self.check_wall_collision()
        # self.rect.x += self.vel_x
        # self.rect.y += self.vel_y

    def check_wall_collision(self):

        tempx = self.rect.x + self.vel_x
        tempy = self.rect.y + self.vel_y
        temp_rect = Rect(tempx, tempy, 30, 30)
        for tile in tiles:
            if temp_rect.colliderect(tile[1]):
                return self.rect.x, self.rect.y
        del(temp_rect)
        return tempx, tempy

#SET ROWS and COLS (CURRENTLY 30 x 30 pixel boxes)
ROWS = 20
COLS = 20

class Gridlines:

    def __init__(self) -> None:
        pass

    def draw(self):
        for row in range(ROWS+1):
            for col in range(COLS+1):
                pygame.draw.line(screen, (255,255,255), start_pos=(col*(screen_width//ROWS),0), end_pos=(col*(screen_width//ROWS),screen_height), width=1)
            pygame.draw.line(screen, (255,255,255), start_pos=(0,row*(screen_height//COLS)), end_pos=(screen_width, row*(screen_height//COLS)), width=1)



class Map:

    def __init__(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if game_map[row][col] == 0:
                    continue
                temp_img = assets[game_map[row][col]]
                temp_rect = Rect(col*(screen_width//COLS),row*(screen_height//ROWS), 30, 30)
                tiles.append((temp_img, temp_rect))

    def draw(self):
        for tile in tiles:
            screen.blit(tile[0], tile[1])



class Cherry:

    def __init__(self) -> None:
        self.img = pygame.transform.scale(pygame.image.load("img/cherry.png"), (30,30))
        self.pos = cherry_positions[randint(0, len(cherry_positions)-1)]

    def draw(self, pl):
        screen.blit(self.img, self.pos)
        self.check_collision(pl)
    
    def check_collision(self, pl):
        temp_rect = Rect(self.pos[0], self.pos[1], 30, 30)
        if temp_rect.colliderect(pl.rect):
            self.pos = cherry_positions[randint(0, len(cherry_positions)-1)]
        del(temp_rect)

grids = Gridlines()
map = Map()
player = Player()
cherry = Cherry()


while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_LEFT:
                player.dir = "LEFT"
            if event.key == K_RIGHT:
                player.dir = "RIGHT"
            if event.key == K_UP:
                player.dir = "UP"
            if event.key == K_DOWN:
                player.dir = "DOWN"
        # if event.type == KEYUP:
        #     if event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or event.key == K_DOWN:
        #         player.moving
    
    screen.fill(BLACK)  #fill black
    #grids.draw()
    map.draw()
    player.draw()
    cherry.draw(player)

    pygame.display.update()
pygame.quit()

