import pygame as pg
from pygame.locals import *
import sys , os
from random import randint
from Nave import *
from pygame import *
from Asteroides import *

FPS = 60
GREEN = (38, 158, 41)
FUCSIA = (236, 52, 234)
RED = (229, 9, 9)
WHITE = (255, 255, 255)

class Game:
    clock = pg.time.Clock()

    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('The Quest')

        self.background_img = pg.image.load('resources/fondo/espacio.jpg').convert()
        
        self.fontGran = pg.font.Font('resources/fonts/gameover.ttf', 40)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 90) 
        
        self.marcador = self.font.render('0', True, WHITE) 
        self.livescounter = self.font.render('5', True, WHITE)       
        self.text_insert_coin = self.font.render("Press   Space", True, FUCSIA)
        self.text_text = self.font.render("Comienza tu aventura", True, GREEN)      
        self.text_gameOver = self.fontGran.render("GAME OVER", True, RED)       
        self.text_titulo = self.font.render("THE QUEST", True, GREEN)

              
        self.player_group = sprite.Group()
        self.asteroid_group = sprite.Group()
        self.all_group = sprite.Group()

        self.meteorito = Meteor()
        self.asteroid_group.add(self.meteorito)

        self.ship = Nave(10, 300)
        self.player_group.add(self.ship)

        self.all_group.add(self.ship, self.asteroid_group)
      
        self.meteor_max = 10
        self.meteor_creados = 0
        self.ultimo_meteor = FPS * 12
        self.nuevo_meteor = FPS// 4
        self.run3()

        print(self.asteroid_group)

    def run3(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/Tune.mp3')
        pg.mixer.music.play()

    def nuevoMeteor(self,dt):
        self.ultimo_meteor += dt
        if self.ultimo_meteor >= self.nuevo_meteor:
            nuevo = Meteor( x=randint(800,1000), y=randint(10, 550))
            nuevo.speed = randint(1,6)
        self.asteroid_group.add(nuevo)
        self.ultimo_meteor = 0

    def quitGame(self):
        pg.quit()
        sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quitGame()

            if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.ship.go_up()

                    if event.key == K_DOWN:
                        self.ship.go_down()
       
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.ship.go_up()
            self.ship.speed +=0.4
        if keys_pressed[K_DOWN]:
            self.ship.go_down()
            self.ship.speed +=0.4
       
        if keys_pressed[K_UP] == False and keys_pressed[K_DOWN] == False:
            self.ship.speed = 5

    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.handleEvents()

            self.screen.blit(self.background_img,(0,0))

            #self.allSprites.update(dt)
            #self.allSprites.draw(self.screen)
            
            self.all_group.update(dt)
            self.all_group.draw(self.screen) 

            pintados = len(self.asteroid_group)
            if pintados < self.meteor_max:
                self.nuevoMeteor(dt)

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.screen)           
            self.screen.blit(self.livescounter, (55, 10))
            self.screen.blit(self.marcador, (685, 10))
            
            print(self.asteroid_group)



            pg.display.flip()
        self.quitGame()

            


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()