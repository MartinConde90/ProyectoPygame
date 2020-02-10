import pygame as pg 
from pygame.locals import *

FPS: 60
class Explosion(pg.sprite.Sprite):
    
    def __init__(self, x=0,y=0):

        self.w = 64
        self.h = 64

        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA,32)
        self.rect = self.image.get_rect()
        

        self.frames = []
        self.index = 0
        self.how_many = 0
        self.animation_time = 30

        self.loadFrames()
        self.current_time = 0

    def loadFrames(self):
        sprite_sheet = pg.image.load('resources/explosions/exp3.png').convert_alpha()
        for fila in range(4):
            y = fila * self.h
            for columna in range(4):
                x = columna * self.w

                image = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))

                
                self.frames.append(image)

        self.how_many = len(self.frames)
        self.image = self.frames[self.index]

    def update(self, dt):
        self.current_time += dt

        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index +=1 

            if self.index >= self.how_many:
                self.index = 0
            
            self.image = self.frames[self.index]