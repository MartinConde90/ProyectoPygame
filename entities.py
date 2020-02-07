import pygame as pg
from pygame.locals import *
from random import randint

FPS = 60

class Nave(pg.sprite.Sprite):
    pictures = 'nave.png'
    speed = 10
    lives = 5

    def __init__(self, x=10, y=300):
        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('resources/{}'.format(self.pictures)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h
        
    def go_up(self):
        self.rect.y = max(0, self.rect.y - self.speed)  
        if self.y <= 0:
            self.rect.y = 0

    def go_down(self):
        self.rect.y = min(self.rect.y + self.speed, 600-self.w)     
        if self.y >= 600:
            self.rect.y = 600 
        
class Meteor(pg.sprite.Sprite):
    picture = "meteoro1.png" 
    picture2 = "meteoro2.png"
    picture3 = "meteoro3.png"
    eleccion = 0
    speed = randint(5,10)
   
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
        pg.sprite.Sprite.__init__(self)

        self.image1 = pg.image.load('resources/meteor/{}'.format(self.picture)).convert_alpha()
        self.image2 = pg.image.load('resources/meteor/{}'.format(self.picture2)).convert_alpha()
        self.image3 = pg.image.load('resources/meteor/{}'.format(self.picture3)).convert_alpha()

        self.listaImagenes = [self.image1, self.image2, self.image3]
        self.posImagen = randint(0,2)

        self.eleccion = self.posImagen   

        self.image = self.listaImagenes[self.eleccion]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h
       
    def update(self, dt):
        self.rect.x = self.rect.x - self.speed 
        self.rect.y = self.rect.y 
        

    
        