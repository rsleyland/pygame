import pygame
import json

class Spritesheet:

    def __init__(self, filename) -> None:
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
    
    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((255,255,255))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data[name]
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x+2, y+2, w-4, h-4)
        return image