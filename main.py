import pygame as pg
from pygame.locals import *
import sys 
from random import randint
from entities import *
from pygame import sprite
from pygame import time

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

        self.background_img = pg.image.load('resources/named.jpg').convert()
        
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

        self.meteorito = Meteor(800, randint(10, 550))
        self.asteroid_group.add(self.meteorito)

        self.ship = Nave(10, 300)
        self.player_group.add(self.ship)

        self.all_group.add(self.ship, self.asteroid_group)


        print(self.meteorito)



    def gameOver(self):
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
            self.livescounter = self.font.render(str(self.ship.lives), True, WHITE)
            
           
            

            self.all_group.update(dt)
            self.all_group.draw(self.screen) 

            self.screen.blit(self.livescounter, (55, 10))
            self.screen.blit(self.marcador, (685, 10))
            
            pg.display.flip()

            


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()