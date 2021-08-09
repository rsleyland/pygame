import pygame, csv
from pygame.locals import *

pygame.init()

margin = 100
myfont = pygame.font.Font(pygame.font.get_default_font(), 30)
myfont_sml = pygame.font.Font(pygame.font.get_default_font(), 16)
show_grid_lines = False
size = screen_width, screen_height = 1000, 1000
grid_width = screen_width - 2*margin
grid_height = screen_height - 2*margin
screen = pygame.display.set_mode(size)
BLACK = 0, 0, 0 
WHITE = 255, 255, 255
mouse_pressed = False
run = True
tile_size = 40
dirt_img = pygame.transform.scale(pygame.image.load('img/dirt.png'), (tile_size, tile_size))
grass_img = pygame.transform.scale(pygame.image.load('img/grass.png'), (tile_size, tile_size))
plat_img = pygame.transform.scale(pygame.image.load('img/platform.png'), (tile_size, tile_size))
apple_img = pygame.transform.scale(pygame.image.load('img/apple.png'), (tile_size, tile_size))
coin_img = pygame.transform.scale(pygame.image.load('img/coin.png'), (tile_size, tile_size))
blob_img = pygame.transform.scale(pygame.image.load('img/blob.png'), (tile_size, tile_size))
current_img_id = 1
image_ids = {1: dirt_img, 2: grass_img, 3: plat_img, 4: apple_img, 5: coin_img, 6: blob_img}
tiles = []
tile_img_ids = [] 
for row in range(grid_height//tile_size):
    for col in range(grid_width//tile_size):
        tiles.append(pygame.draw.rect(screen, BLACK, rect=(col*tile_size+margin, row*tile_size+margin, tile_size, tile_size), width=1))
        tile_img_ids.append(0)


def select_tile(pos):
    for i, tile in enumerate(tiles):
        if tile.collidepoint(pos):
            tile_img_ids[i] = current_img_id

def change_tile():
    global current_img_id
    current_img_id = current_img_id+1
    if current_img_id == 7:
        current_img_id = 0


# tile id's to read from if editing exisiting map, comment if not loading map
tile_img_ids = [  
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,1,
1,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,0,0,1,
1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,4,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,1,
1,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,
1,0,0,4,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,1,
1,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,1,
1,0,0,0,2,2,2,1,1,1,1,2,0,0,0,0,0,0,0,1,
1,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,4,0,1,
1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,
]

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_s:
                change_tile()
        if event.type == MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == MOUSEBUTTONUP:
            mouse_pressed = False
    screen.fill(WHITE)  #fill WHITE

    #update tile selector preview
    text = myfont.render('Current Tile: ', False, (0, 0, 0))
    hint = myfont_sml.render('Press "S" to change tile', False, (0, 0, 0))
    screen.blit(text, (10, 15))
    screen.blit(hint, (10, 65))
    if current_img_id == 0:
        pygame.draw.rect(screen, BLACK, rect=(200, 10, tile_size, tile_size), width=1)
    else:
        screen.blit(image_ids[current_img_id], (200, 10))


    if mouse_pressed:
        click_pos = pygame.mouse.get_pos()
        select_tile(click_pos)

    for i, tile_id in enumerate(tile_img_ids):
        if tile_id == 0:
            if show_grid_lines:
                pygame.draw.rect(screen, BLACK, rect=tiles[i], width=1)
        else:
            screen.blit(image_ids[tile_id], tiles[i])
    pygame.display.update()




for row in range(grid_height//tile_size):
    for col in range(grid_width//tile_size):
        print(tile_img_ids[(row*(grid_width//tile_size))+col], end=',')
    print()


with open("output_level.csv", 'w') as f:
    csv_writer = csv.writer(f)
    for row in range(grid_height//tile_size):
        row_list = []
        for col in range(grid_width//tile_size):
            row_list.append(tile_img_ids[(row*(grid_width//tile_size))+col])
        row_list.append('')
        csv_writer.writerow(row_list)


with open("output_game.txt", 'w') as f:
    output = "["
    for row in range(grid_height//tile_size):
        row_list = "["
        for col in range(grid_width//tile_size):
            row_list+= f"{(tile_img_ids[(row*(grid_width//tile_size))+col])}, "
        row_list+="]"
        output+= row_list+",\n"
    output+= "]"
    f.write(output)


pygame.quit()