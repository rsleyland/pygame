import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)
BLACK = 0, 0, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Platformer")
runner_imgs = [pygame.image.load(f"img/player/Run/0.png"), pygame.image.load(f"img/player/Run/1.png"), pygame.image.load(f"img/player/Run/2.png"),
    pygame.image.load(f"img/player/Run/3.png"), pygame.image.load(f"img/player/Run/4.png"), pygame.image.load(f"img/player/Run/5.png")]

# clock = pygame.time.Clock()
# FPS = 60

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        img = pygame.image.load(f"img/player/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = speed
        self.scale = scale
        self.velx = 0
        self.vely = 0
        self.running = False
        self.runCount = 0
        self.flip = 0


    def move_left(self):
        self.velx = -self.speed

    def move_right(self):
    #     if self.facing == "LEFT":
    #         self.image = pygame.transform.flip(self.image, True, False)
        self.velx = self.speed

    def draw(self):

        img = pygame.image.load(f"img/player/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width()*self.scale), int(img.get_height()*self.scale)))

        if self.running:
            img = runner_imgs[self.runCount]
            self.image = pygame.transform.scale(img, (int(img.get_width()*self.scale), int(img.get_height()*self.scale)))
            self.runCount +=1
            if self.runCount == 5: self.runCount = 0

        self.x += self.velx

        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)


player = Soldier(200, 200, 2, 5)
run = True

while run:
    # clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                    player.flip = 1
                    player.running = True
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                    player.flip = 0
                    player.running = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.velx = 0
                    player.running = False

    player.draw()               
    pygame.display.update()


pygame.quit()