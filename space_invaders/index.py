import pygame
from pygame.locals import *
from random import randint
pygame.init()




size = screen_width, screen_height = 600, 600
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
run = True
bg_img = pygame.transform.scale(pygame.image.load("img/bg.png").convert(), (screen_width, screen_height))
ss_bullets = []
alien_bullets = []
aliens = []
alien_rows = []
shooting = False
shooting_delay_count = 0
alien_spawn_delay = 0
alien_move_count = 0
explosions = []
explosion_sound_1 = pygame.mixer.Sound("img/explosion.wav")
explosion_sound_1.set_volume(0.1)
FPS = 60
clock = pygame.time.Clock()

class Spaceship:

    def __init__(self) -> None:
        self.pos_x = screen_width/2-25
        self.pos_y = screen_height*0.8
        self.ss_img = pygame.transform.scale(pygame.image.load("img/spaceship.png").convert(), (50,50))
        self.dir = None
        self.rect = self.ss_img.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def draw(self):
        self.move()
        screen.blit(self.ss_img, (self.pos_x, self.pos_y))
        self.rect = self.ss_img.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
    
    def move(self):
        if self.dir == "LEFT":
            self.pos_x -=5
            if self.pos_x< -50:
                self.pos_x = screen_width
        if self.dir == "RIGHT":
            self.pos_x +=5
            if self.pos_x > screen_width:
                self.pos_x = -50

spaceship = Spaceship()

class Explosion:

    def __init__(self, posx, posy) -> None:
        self.imgs = [ 
            pygame.transform.scale(pygame.image.load("img/exp1.png").convert(), (25, 25)),
            pygame.transform.scale(pygame.image.load("img/exp2.png").convert(), (25, 25)),
            pygame.transform.scale(pygame.image.load("img/exp3.png").convert(), (25, 25)),
            pygame.transform.scale(pygame.image.load("img/exp4.png").convert(), (25, 25)),
            pygame.transform.scale(pygame.image.load("img/exp5.png").convert(), (25, 25))
        ]
        self.pos_x = posx
        self.pos_y = posy
        self.img_count = 0
        self.exp_count = 0
        pygame.mixer.Sound.play(explosion_sound_1)

    def draw(self):
        if self.img_count < 5:
            screen.blit(self.imgs[self.img_count], (self.pos_x, self.pos_y))
        else:
            explosions.remove(self) 
        self.exp_count += 1
        if self.exp_count == 5:
            self.exp_count = 0
            self.img_count+=1


class SS_Bullet:
    def __init__(self) -> None:
        self.bullet_img = pygame.transform.scale(pygame.image.load("img/bullet.png").convert(), (5, 5))
        self.rect = self.bullet_img.get_rect()
        self.rect.x = spaceship.pos_x+20
        self.rect.y = spaceship.pos_y

    def draw(self):
        screen.blit(self.bullet_img, (self.rect.x, self.rect.y))
        self.rect[1] -= 5
        if self.rect[1] < 0:
            ss_bullets.remove(self)
        self.collisionCheck()

    def collisionCheck(self):
        for alien in aliens:
            if self.rect.colliderect(alien.rect):
                aliens.remove(alien)    
                explosions.append(Explosion(alien.rect[0], alien.rect[1]))

                #CODE BELOW WILL ENSURE THE ALIENS TRAVERSE THE WHOLE SCREEN WIDTH (closest alien to edge will go to the edge)
                # NEEDS extra code to only move down rows above when the row below is ready to move down (CBA)
                # for row in alien_rows:
                #     try:
                #         row.row.remove(alien)
                #         break
                #     except:
                #         continue
                


class Alien:

    def __init__(self, pos_x, pos_y, id) -> None:
        self.alien_img = pygame.transform.scale(pygame.image.load(f"img/alien{id}.png").convert(), (25, 25))
        self.id = id
        self.rect = self.alien_img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.shoot_count = 0
        self.shoot_limit = randint(len(aliens)*10, len(aliens)*20)

    def draw(self):
        screen.blit(self.alien_img, self.rect)
        if self.shoot_count == self.shoot_limit:
            alien_bullets.append(Alien_Bullet(self.rect.centerx, self.rect.bottom))
            self.shoot_count = 0
            self.shoot_limit= randint(len(aliens)*10, len(aliens)*20)
        self.shoot_count+=1
        

class AlienRow:

    def __init__(self) -> None:
        x_pos = 50
        self.row = []
        self.dir = "RIGHT"
        self.move_count = 0
        for i in range(10):
            temp = Alien(x_pos, 50, randint(1,5))
            aliens.append(temp)
            self.row.append(temp)
            x_pos += 50


    def move_(self):
        self.move()
        # if self.move_count == 0:
        #     self.move()
        # self.move_count +=1
        # if self.move_count == 3:
        #     self.move_count = 0

    def move(self):
        for alien in self.row:
            if self.dir == "RIGHT":
                alien.rect[0] += 1
                if alien.rect[0] > screen_width:
                    self.dir = "LEFT"
                    for alien in self.row:
                        alien.rect[1] += 15
            else:
                alien.rect[0] -= 1
                if alien.rect[0] < 0:
                    self.dir = "RIGHT"
                    for alien in self.row:
                        alien.rect[1] += 15

class Alien_Bullet:
    def __init__(self, pos_x, pos_y) -> None:
        self.bullet_img = pygame.transform.scale(pygame.image.load("img/alien_bullet.png").convert(), (5, 5))
        self.rect = self.bullet_img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.move_limit = 0

    def draw(self):
        screen.blit(self.bullet_img, (self.rect.x, self.rect.y))
        self.rect[1] += 3
        # if self.move_limit == 0:
        #     self.rect[1] += 1
        # self.move_limit +=1
        # if self.move_limit == 3:
        #     self.move_limit = 0
        if self.rect[1] > screen_height:
            alien_bullets.remove(self)
        self.collisionCheck()

    def collisionCheck(self):
        global run
        if self.rect.colliderect(spaceship.rect):
            print("GAMEOVER")
            run = False

while run:

    clock.tick(FPS)

    #EVENT GRABBING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_LEFT:
                spaceship.dir = "LEFT"
            if event.key == K_RIGHT:
                spaceship.dir = "RIGHT"
            if event.key == K_SPACE:
                shooting = True
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                spaceship.dir = None
            if event.key == K_SPACE:
                shooting = False
                shooting_delay_count = 0
    
    #DRAW THE BACKGROUND IMAGE
    screen.blit(bg_img, (0,0))

    #SPAWN ALIENS
    if alien_spawn_delay == 0:
        alien_rows.append(AlienRow())
    alien_spawn_delay+=1
    if alien_spawn_delay == 500:
        alien_spawn_delay = 0

    #FIRE THE LASERS
    if shooting and shooting_delay_count==0:
        ss_bullets.append(SS_Bullet())
    shooting_delay_count +=1
    if shooting_delay_count == 10:
        shooting_delay_count = 0

    # DRAW THE IMAGES    
    for bullet in ss_bullets:
        bullet.draw()
    for row in alien_rows:
        row.move_()
    for alien in aliens:
        alien.draw()
    spaceship.draw()

    #EXPLOSIONS
    for e in explosions:
        e.draw()

    #ALIEN BULLETS
    for bullet in alien_bullets:
        bullet.draw()


    pygame.display.update()

pygame.quit()