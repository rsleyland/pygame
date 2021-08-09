import pygame
from pygame.locals import *
from random import randint

pygame.init()

exit = False

while not exit:

    size = screen_width_full, screen_height_full = 801, 900
    screen_height = screen_height_full-100
    screen_width = screen_width_full-1
    screen = pygame.display.set_mode(size)
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    run = True
    clock = pygame.time.Clock()
    FPS = 8
    text_font = pygame.font.Font(pygame.font.get_default_font(), 40)
    text_font_sml = pygame.font.Font(pygame.font.get_default_font(), 28)
    apple = None
    crash = False
    margin_top = 100
    score = 0

    class Snake:

        def __init__(self) -> None:
            self.x = screen_width//2 
            self.y = screen_height//2 +margin_top
            self.size = 20
            self.vel_x = 20
            self.vel_y = 0
            self.length = 1
            self.tails = []
            self.tails.append((self.x, self.y))

        def draw(self):
            self.x +=self.vel_x
            self.y +=self.vel_y

            if self.x < 0:
                self.x = screen_width-self.size
            elif self.x > screen_width-self.size:
                self.x = 0
            elif self.y < margin_top:
                self.y = screen_height-self.size +margin_top
            elif self.y > screen_height-self.size +margin_top:
                self.y = margin_top

            for tail in self.tails:
                pygame.draw.rect(screen, WHITE, (tail[0], tail[1], self.size, self.size), 1)

            
            self.tails.insert(0, (self.x, self.y))
            if not self.check_collision_apple():    # dont remove last tail if we hit an apple as we want the snake to "GROW"
                self.tails.pop()

            if self.check_collision_self():
                global run, crash
                crash = True
                run = False


        def move(self, dir):
            if dir == "U":
                self.vel_x = 0
                self.vel_y = -20
            elif dir == "D":
                self.vel_x = 0
                self.vel_y = 20
            elif dir == "L":
                self.vel_x = -20
                self.vel_y = 0
            else:
                self.vel_x = 20
                self.vel_y = 0

        def check_collision_apple(self):
            global apple, score
            if Rect(self.tails[0][0], self.tails[0][1], self.size, self.size).collidepoint(apple.x+10, apple.y+10):
                apple = Apple()
                self.length +=1
                score+= 10
                return True
            return False

        def check_collision_self(self):
            if len(self.tails)==1:
                return False
            for i1, tail1 in enumerate(self.tails):
                for i2, tail2 in enumerate(self.tails):
                    if Rect(tail1[0], tail1[1], self.size, self.size).colliderect(Rect(tail2[0], tail2[1], self.size, self.size)) and i1 != i2:
                        return True

    s = Snake()

    class Apple:

        def __init__(self) -> None:
            self.x = 0
            self.y = 0
            self.find_clear_pos()
            self.rect = None

        def find_clear_pos(self):
            self.x = randint(0, screen_width//s.size-1)*s.size
            self.y = randint(0, screen_height//s.size-1)*s.size + margin_top
            while True:
                collision = False
                for tail in s.tails:
                    if Rect(tail[0], tail[1], s.size, s.size).collidepoint((self.x+5, self.y+5)):
                        collision = True
                        break
                if collision:
                    self.x = randint(0, screen_width//s.size-1)*s.size 
                    self.y = randint(0, screen_height//size-1)*s.size + margin_top
                else:
                    break

        def draw(self):
            self.rect = pygame.draw.circle(screen, WHITE, (self.x+(s.size//2), self.y+(s.size//2)), 10)
                    
    apple = Apple()



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                run = False
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit = True
                    run = False
                    break
                elif event.key == K_UP:
                    s.move("U")
                elif event.key == K_DOWN:
                    s.move("D")
                elif event.key == K_LEFT:
                    s.move("L")
                elif event.key == K_RIGHT:
                    s.move("R")
        
        

        screen.fill(BLACK)  #fill black

        #display score and draw boundary border
        score_text = text_font_sml.render(f"Score: {score}", False, WHITE)
        screen.blit(score_text, (50, 40))
        pygame.draw.line(screen, WHITE, start_pos=(0, 100), end_pos=(screen_width, 100))
        pygame.draw.line(screen, WHITE, start_pos=(0, 100), end_pos=(0, screen_height_full))
        pygame.draw.line(screen, WHITE, start_pos=(screen_width, 100), end_pos=(screen_width, screen_height_full))
        pygame.draw.line(screen, WHITE, start_pos=(0, screen_height_full-1), end_pos=(screen_width, screen_height_full-1))

        s.draw()
        apple.draw()
        pygame.display.update()


    if crash :run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    exit = True
                if event.key == K_RETURN:
                    run = False
                    print("HIHIHI")


        screen.fill(BLACK)  #fill black

        game_over_text = text_font.render("Game Over", False, WHITE)
        game_over_text_sml = text_font_sml.render("Press enter to Restart", False, WHITE)
        screen.blit(game_over_text, (screen_width//2-100, screen_height//2))
        screen.blit(game_over_text_sml, (screen_width//2-150, screen_height//2+50))
        pygame.display.update()
    
    pygame.display.update()

pygame.quit()