import sys, pygame
from track import TrackBuilder


pygame.init()

size = width, height = 480, 480
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
DIRECTIONS = {pygame.K_LEFT: 'Left', pygame.K_UP: 'Up', pygame.K_RIGHT: 'Right', pygame.K_DOWN: 'Down'}


screen = pygame.display.set_mode(size)
tb = TrackBuilder()
tb.build_track(width, height)


while True:

    game_status = "On"
    player_pos = [width/4, height-6]
    player_xvel = 0
    player_yvel = 0
    player = None
                
    while game_status == "On":

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #print(pygame.mouse.get_pos())
                if player:
                    print(player)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_xvel -= 2
                elif event.key == pygame.K_UP:
                    player_yvel -= 2
                elif event.key == pygame.K_RIGHT:
                    player_xvel += 2
                elif event.key == pygame.K_DOWN:
                    player_yvel += 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_xvel = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_yvel = 0
        
        player_pos[0] += player_xvel
        player_pos[1] += player_yvel
        lines = []
        for section in tb.sections:
            lines.append(pygame.draw.line(surface=screen, color=WHITE, start_pos=(section.startx, section.starty), end_pos=(section.endx, section.endy), width=section.width))
        # lines.append(pygame.draw.line(surface=screen, color=WHITE, start_pos=(width/4, height), end_pos=(width/4, height/2), width=30))
        # lines.append(pygame.draw.line(surface=screen, color=WHITE, start_pos=(width/4-14, height/2), end_pos=(3*width/4, height/2), width=30))
        # lines.append(pygame.draw.line(surface=screen, color=WHITE, start_pos=(3*width/4, height/2+15), end_pos=(3*width/4, 0), width=30))
        
        player = pygame.draw.circle(surface=screen, color=RED, center=(player_pos[0], player_pos[1]), radius=5, width=0)

        crash = False
        inside = False
        for line in lines:
            if line.contains(player):
                inside = True
        if not inside : crash = True
        
        if crash:
            game_status = "Off"

        pygame.display.flip()

    


# pygame.draw.rect(surface=screen, color=tile[2], rect=(tile[0],tile[1],24, 24), width=0, border_radius=0)