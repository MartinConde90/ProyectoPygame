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

        self.background_img = pg.image.load('resources/fondo/espacio1.jpg').convert()
        self.background_story = pg.image.load('resources/fondo/Reference2.jpg').convert()
        self.background_menu = pg.image.load('resources/fondo/unnamed.jpg').convert()
        self.background_rules = pg.image.load('resources/fondo/controls.jpg').convert()
        self.UP = pg.image.load('resources/up.png').convert().convert_alpha()
        self.DOWN = pg.image.load('resources/down.png').convert().convert_alpha()


        self.fontGran = pg.font.Font('resources/fonts/gameover.ttf', 40)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 90) 
        self.fontC = pg.font.Font('resources/fonts/PressStart.ttf', 30)
        self.fontR = pg.font.Font('resources/fonts/text.ttf', 30)
        
        self.marcador = self.font.render('0', True, WHITE) 
        self.livescounter = self.font.render('5', True, WHITE)       
        self.text_insert_coin = self.fontC.render("Press   Spacebar", True, FUCSIA)
        self.text_text = self.font.render("Comienza tu aventura", True, GREEN)      
        self.text_gameOver = self.fontGran.render("GAME OVER", True, RED)       
        self.text_titulo = self.font.render("THE QUEST", True, GREEN)

        self.text_controlesU = self.fontR.render("Pulsa           para    subir", True, GREEN)
        self.text_controlesD = self.fontR.render("Pulsa           para    bajar", True, GREEN)
        self.text_controlesS = self.fontR.render("Manten pulsado          o          para aumentar la velocidad", True, GREEN)
        self.text_return = self.fontC.render("Press   Spacebar   to   return", True, FUCSIA)
        self.text_instructions = self.fontR.render("Press I to see instructions", True, WHITE)
        self.text_story = self.fontR.render("Press S  to know your story", True, WHITE)
              
        self.player_group = sprite.Group()
        self.asteroid_group = sprite.Group()
        self.all_group = sprite.Group()

        self.meteorito = Meteor()
        self.asteroid_group.add(self.meteorito)

        self.ship = Nave(10, 300)
        self.player_group.add(self.ship)

        self.all_group.add(self.ship, self.asteroid_group)
        self.default_font = pg.font.Font(None, 28)
        self.meteor_max = 10
        self.meteor_creados = 0
        self.ultimo_meteor = FPS * 12
        self.nuevo_meteor = FPS// 4
        #self.run3()
        #self.run2()

    def run3(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/FX2.mp3')
        pg.mixer.music.play()
    def run2(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/open.mp3')
        pg.mixer.music.play()

    def nuevoMeteor(self,dt):
        self.ultimo_meteor += dt
        if self.ultimo_meteor >= self.nuevo_meteor:
            nuevo = Meteor( x=randint(800,1000), y=randint(10, 550))
            nuevo.speed = randint(1,6)
        self.asteroid_group.add(nuevo)
        self.ultimo_meteor = 0

    def quitGame(self):
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                    pg.quit()
                    sys.exit()

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

    def start_screen(self):
        while True:
            self.screen.blit(self.background_menu,(0,0))
            self.screen.blit(self.text_titulo,(100,100))
            self.screen.blit(self.text_insert_coin,(235,330)) 
            self.screen.blit(self.text_instructions,(50,560))
            self.screen.blit(self.text_story,(500,560))
            
            pg.display.update()
            for event in pg.event.get():

                if event.type == KEYDOWN:
                        if event.key == K_i:
                            self.run3()
                            self.rules_screen()
                            return
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.run2()
                            self.mainloop()
                            return
                if event.type == KEYDOWN:
                        if event.key == K_s:
                            self.run3()
                            self.Story()
                            return

                if event.type == QUIT:
                        pg.quit()
                        sys.exit()
    
    def rules_screen(self):
        while True:
            self.screen.blit(self.background_rules,(0,0))
            self.screen.blit(self.text_controlesU,(100, 100))
            self.screen.blit(self.text_controlesD,(100,200))
            self.screen.blit(self.UP,(170,100))
            self.screen.blit(self.DOWN,(170,200))            
            self.screen.blit(self.text_controlesS,(100,300))
            self.screen.blit(self.UP,(340,300))
            self.screen.blit(self.DOWN,(270,300))
            self.screen.blit(self.text_return,(100,560))

            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.run3() 
                            self.start_screen()
                            return
    
    def Story(self):
        while True:
            self.screen.blit(self.background_story,(-300,-150))
            
            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.run3()
                            self.start_screen()
                            return

    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.handleEvents()


            #Aqui colisiones#


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
            
            print(self.meteorito.contador)

            pg.display.flip()
        self.quitGame()

            


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.start_screen()