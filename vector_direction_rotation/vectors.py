import pygame

pygame.init()

size = width, height = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
run = True


class Guy:

    def __init__(self, x, y) -> None:
        self.pos = [x, y]
        self.dir = pygame.Vector2(0, -1)    #FACING NORTH TO BEGIN
        self.speed = 5
        self.moving = False
        self.turning = ''

    def move(self):
        self.pos[0] += self.dir[0]*self.speed
        self.pos[1] += self.dir[1]*self.speed

    def turn(self, direc):
        if direc == 'L':    #LEFT TURN
            self.dir = self.dir.rotate(-10)
        elif direc == 'R':    #RIGHT TURN
            self.dir = self.dir.rotate(10)

    def draw(self):
        if self.turning:
            self.turn(self.turning)
        if self.moving:
            self.move()

        s = pygame.Surface((20,20))
        s = s.convert_alpha()
        s.fill(BLACK)
        pygame.draw.rect(s, WHITE, (0, 0, 20, 20), 0)
        s = pygame.transform.rotate(s,-pygame.Vector2(0, 0).angle_to(self.dir))
        screen.blit(s, self.pos)

player = Guy(100, 100)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.turning = 'L'
            if event.key == pygame.K_RIGHT:
                player.turning = 'R'
            if event.key == pygame.K_UP:
                player.moving = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.turning = ''
            if event.key == pygame.K_UP:
                player.moving = False

    screen.fill(BLACK)
    player.draw()
    pygame.display.update()
    


pygame.quit()

