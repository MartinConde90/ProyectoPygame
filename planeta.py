import pygame as pg
from pygame.locals import *

FPS = 60

class Planeta(pg.sprite.Sprite):
    pictures = 'PlanetRaw.png'
    speed = 1
    

    def __init__(self, x=800, y=-50):
        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.image.load('resources/planeta/PlanetRaw.png').convert_alpha()      

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h
    
    def update(self, dt):
        if self.rect.x > 599:
            self.rect.x = self.rect.x - self.speed
        
            
