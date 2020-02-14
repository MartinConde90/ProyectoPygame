import pygame as pg
from pygame.locals import *
from random import randint

candidatos = 0
class Meteor(pg.sprite.Sprite):
    picture = ["G17.png" ,"F17.png","E16.png","D15.png" ,"C5.png","B13.png","A3.png"]
    picture1 = ["meteoro1.png" ,"meteoro2.png","meteoro3.png"]
    
    speed = randint(1,4)
    
    def __init__(self, x=randint(800,1000), y=randint(10, 550)):
        self.x = x
        self.y = y
    
        pg.sprite.Sprite.__init__(self)
        
        self.tiempo =  pg.time.get_ticks()
        
        
        self.image = pg.image.load('resources/meteor/{}'.format(self.picture1[randint(0,2)])).convert_alpha()
        
        if self.tiempo > 6802:
            self.image = pg.image.load('resources/meteor/{}'.format(self.picture[randint(0,3)])).convert_alpha()
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h

    def update(self, dt):
        self.rect.x = self.rect.x - self.speed        
        if self.rect.x <=  0 - self.w:           
            self.kill() 
            del self 
    
    def test_collide(self, group):
        self.candidatos = pg.sprite.spritecollide(self, group, True)
    
    
        