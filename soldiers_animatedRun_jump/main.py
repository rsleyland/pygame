import pygame
from pygame.constants import K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_a, K_d, K_w
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)
BLACK = 0, 0, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()
FPS = 60

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, player_type) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.p_type = "enemy" if player_type == "enemy" else "player"
        img = pygame.image.load(f"img/{self.p_type}/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.scale = scale
        self.speed = speed
        self.acc = 0
        self.velx = 0
        self.vely = 0
        self.tempy = 0
        self.jumping = False
        self.running = False
        self.runCount = 0
        self.flip = 0

    def draw(self):
        
        img = pygame.image.load(f"img/{self.p_type}/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width()*self.scale), int(img.get_height()*self.scale)))

        if self.running:
            img = img = pygame.image.load(f"img/{self.p_type}/Run/{self.runCount}.png")
            self.image = pygame.transform.scale(img, (int(img.get_width()*self.scale), int(img.get_height()*self.scale)))
            self.runCount +=1
            if self.runCount == 5: self.runCount = 0

        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)

        self.x += self.velx
        self.y += self.vely
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
        if self.y > self.tempy-20:
            self.vely =0
            self.acc =0
            self.jumping = False
        else:
            self.vely += self.acc

        if self.x < 0:
            self.x = SCREEN_WIDTH
        if self.x > SCREEN_WIDTH:
            self.x = 0

    def jump(self):
        if self.jumping:
            return
        self.jumping = True
        self.tempy = self.y
        self.vely = -20
        self.acc = 2

    def move_left(self):
        self.velx -= self.speed
    
    def move_right(self):
        self.velx += self.speed

    def stop(self):
        self.velx = 0

player = Soldier(200, 200, 2, 5, "player")
enemy = Soldier(400, 200, 2, 3, 'enemy')

run = True

while run:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    player.jump()
                if event.key == K_LEFT:
                    player.move_left()
                    player.running = True
                    player.flip = 1
                if event.key == K_RIGHT:
                    player.move_right()
                    player.flip = 0
                    player.running = True
                if event.key == K_w:
                    enemy.jump()
                if event.key == K_a:
                    enemy.move_left()
                    enemy.running = True
                    enemy.flip = 1
                if event.key == K_d:
                    enemy.move_right()
                    enemy.running = True
                    enemy.flip = 0
                if event.key == K_ESCAPE:
                    run = False
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    player.stop()
                    player.running = False
                if event.key == K_a or event.key == K_d:
                    enemy.stop()
                    enemy.running = False
                

    
    player.draw()
    enemy.draw()
    pygame.display.update()
    


pygame.quit()

