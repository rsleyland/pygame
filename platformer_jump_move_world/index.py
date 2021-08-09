import pygame
from pygame.locals import *

pygame.init()

size = screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Platformer')
screen.fill((0,0,0))
run = True
score = 0
#define game variables
tile_size = 50
score_font = pygame.font.Font(pygame.font.get_default_font(), 24)

#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
#sun_img = pygame.transform.scale2x(sun_img)
sun_img_rect = sun_img.get_rect()
sun_img_rect.left = 100
sun_img_rect.top = 100
screen_scroll = 0
screen_thresh = 100


class World():
    def __init__(self, data) -> None:
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        plat_img = pygame.transform.scale(pygame.image.load('img/platform.png'), (tile_size, tile_size))
        apple_img = pygame.transform.scale(pygame.image.load('img/apple.png'), (tile_size, tile_size))
        coin_img = pygame.transform.scale(pygame.image.load('img/coin.png'), (tile_size, tile_size))
        blob_img = pygame.transform.scale(pygame.image.load('img/blob.png'), (tile_size, tile_size))
        apple_img = pygame.image.load('img/apple.png')
        row_count = 0
        for row in data:
            col_count = 0
            for col in row:
                if col == 1:
                    self.create_tile(dirt_img, col_count, row_count, 1)
                elif col == 2:
                    self.create_tile(grass_img, col_count, row_count, 2)
                elif col == 3:
                    self.create_tile(plat_img, col_count, row_count, 3)
                elif col == 4:
                    self.create_tile(apple_img, col_count, row_count, 4)
                elif col == 5:
                    self.create_tile(coin_img, col_count, row_count, 5)
                elif col == 6:
                    self.create_tile(blob_img, col_count, row_count, 6)
                col_count += 1
            row_count += 1

    def create_tile(self, type, cc, rc, num):
        img = pygame.transform.scale(type, (tile_size, tile_size))
        img_rect = img.get_rect()
        img_rect.x = cc*tile_size
        img_rect.y = rc*tile_size
        self.tile_list.append((img, img_rect, num))


    def draw(self):
        global screen_scroll
        for tile in self.tile_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])

world_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, ],
[1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 1, ],
[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1, ],
[1, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, ],
[1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, ],
[1, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 4, 0, 1, ],
[1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, ],
]
world = World(world_data)

class Player():

    def __init__(self, x, y) -> None:
        self.image = pygame.transform.scale(pygame.image.load('img/guy1.png'), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.running = False
        self.direction = ''
        self.anim_count = 1
        self.flip = 0
        self.vel_y = 0
        self.jumping = False
        self.gravity = 2
        self.grounded = True
        self.falling = False

    def move(self, dir):
        global screen_scroll
        screen_scroll = 0
        dx = 0
        if dir == "LEFT":
            newx = self.rect.x-6    #new position x co-ordinate - NEXT check for collison
            if self.check_collision(newx, self.rect.y, 40, 80):
                return  #if move hits wall then dont do move
            dx = -6
            self.flip = 1
        else:
            newx = self.rect.x+6    #new position x co-ordinate - NEXT check for collison
            if self.check_collision(newx, self.rect.y, 40, 80):
                return  #if move hits wall then dont do move
            dx = 6
            self.flip = 0

        self.rect.x += dx

        if self.running and self.rect.left <= screen_thresh:
            screen_scroll = 6
            self.rect.x += -dx
        elif self.running and self.rect.right >= screen_width-screen_thresh:
            screen_scroll = -6
            self.rect.x += -dx

    def jump(self):
        if not self.jumping and self.vel_y < 20:
            self.jumping = True
            self.grounded = False
            self.vel_y = -25

    def check_collision(self, x, y, w ,h):
        global score
        for entry in world.tile_list:
            if entry[1].colliderect(pygame.Rect(x, y, w, h)):
                if entry[2] == 4 or entry[2] == 5:
                    if entry[2] == 4:
                        score+= 1
                    elif entry[2] == 5:
                        score+= 5
                    world.tile_list.remove(entry)
                    break
                self.jumping = False
                return True
        return False


    def draw(self):
        global screen_scroll
        if self.running:
            self.move(self.direction)
            self.image = pygame.transform.scale(pygame.image.load(f'img/guy{self.anim_count}.png'), (40, 80))
            self.image = pygame.transform.flip(self.image, self.flip, 0)
            self.anim_count += 1
            if self.anim_count == 5: self.anim_count = 1
        else:
            screen_scroll = 0

        self.vel_y += self.gravity 
        if self.vel_y > 20:
            self.vel_y = 20

        if not self.grounded:
            
            temp_y = self.rect.y + self.vel_y
            if not self.check_collision(self.rect.left, temp_y, 40, 80):
                self.rect.y = self.rect.y + self.vel_y
            else:
                self.vel_y = 0
        else:
            self.vel_y = 10

        self.grounded = self.check_collision(self.rect.left, self.rect.bottom, 40, 2)

        screen.blit(self.image, self.rect)




player = Player(150, screen_height - 180)

while run:

    

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, sun_img_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_LEFT:
                player.running = True
                player.direction = 'LEFT'
            if event.key == K_RIGHT:
                player.running = True
                player.direction = 'RIGHT'
            if event.key == K_SPACE:
                player.jump()
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.running = False
                player.direction = ''

    
    #display tiles
    world.draw()

    #display player
    player.draw()

    #display score
    score_text = score_font.render(f"Score: {score}", False, (0, 0, 0))
    screen.blit(score_text, (20, 10))

    pygame.display.update()


pygame.quit()