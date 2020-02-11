import pygame as pg
from pygame.locals import *
import sys , os

GREEN = (38, 158, 41)
FUCSIA = (236, 52, 234)
RED = (229, 9, 9)
WHITE = (255, 255, 255)

class Pantallas(pg.sprite.Sprite):
    
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pg.sprite.Sprite.__init__(self)

        self.fontGran = pg.font.Font('resources/fonts/gameover.ttf', 150)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 90) 
        self.fontC = pg.font.Font('resources/fonts/PressStart.ttf', 30)
        self.fontR = pg.font.Font('resources/fonts/text.ttf', 30)



        self.background_img = pg.image.load('resources/fondo/espacio1.jpg').convert()
        self.background_story = pg.image.load('resources/fondo/Reference2.jpg').convert()
        self.background_menu = pg.image.load('resources/fondo/unnamed.jpg').convert()
        self.background_rules = pg.image.load('resources/fondo/controls.jpg').convert()
        self.UP = pg.image.load('resources/up.png').convert().convert_alpha()
        self.DOWN = pg.image.load('resources/down.png').convert().convert_alpha()
        
        self.marcador = self.font.render('0', True, WHITE)        
        self.text_insert_coin = self.fontC.render("Press   Spacebar", True, FUCSIA)
        self.text_text = self.font.render("Comienza tu aventura", True, GREEN)      
        self.text_gameOver = self.fontGran.render("GAME OVER", True, RED)       
        self.text_titulo = self.font.render("THE QUEST", True, GREEN)

        self.text_controlesU = self.fontR.render("Pulsa           para    subir", True, GREEN)
        self.text_controlesD = self.fontR.render("Pulsa           para    bajar", True, GREEN)
        self.text_controlesS = self.fontR.render("Manten pulsado          o          para aumentar la velocidad", True, GREEN)
        self.text_controlesE = self.fontR.render("Pulsa            para salir del juego", True, GREEN)
        self.text_return = self.fontC.render("Press   Spacebar   to   return", True, FUCSIA)
        self.text_instructions = self.fontR.render("Press I to see instructions", True, WHITE)
        self.text_story = self.fontR.render("Press S  to know your story", True, WHITE)

    def run1(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/Tune.mp3')
        pg.mixer.music.play()
    def run2(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/open.mp3')
        pg.mixer.music.play()
    def run3(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/FX2.mp3')
        pg.mixer.music.play()
    def run4(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/play.mp3')
        pg.mixer.music.play()
   
    def Inicial(self):
        while True:
                self.screen.blit(self.background_menu,(0,0))
                rect = self.text_titulo.get_rect()
                self.screen.blit(self.text_titulo,((800 - rect.w)//2,100))
                rect = self.text_insert_coin.get_rect()
                self.screen.blit(self.text_insert_coin,((800 - rect.w)//2,330)) 
                self.screen.blit(self.text_instructions,(50,560))
                self.screen.blit(self.text_story,(500,560))
                pg.display.update()
                
                

    def Instrucciones(self):
        while True:
            self.screen.blit(self.background_rules,(0,0))
            self.screen.blit(self.text_controlesU,(100, 100))
            self.screen.blit(self.text_controlesD,(100,200))
            self.screen.blit(self.UP,(170,100))
            self.screen.blit(self.DOWN,(170,200))            
            self.screen.blit(self.text_controlesS,(100,300))
            self.screen.blit(self.text_controlesE,(100,400))
            self.screen.blit(self.UP,(340,300))
            self.screen.blit(self.DOWN,(270,300))
            rect = self.text_return.get_rect()
            self.screen.blit(self.text_return,((800 - rect.w)//2,560))
            pg.display.update()


    def Historia(self):
        while True:
            self.screen.blit(self.background_story,(-300,-150))
            rect = self.text_return.get_rect()
            self.screen.blit(self.text_return,((800 - rect.w)//2,560))
            pg.display.update()
            

    def FinPartida(self):
        while True:
            rect = self.text_gameOver.get_rect()
            self.screen.blit(self.text_gameOver, ((800 - rect.w)//2, 200))
            rect = self.text_insert_coin.get_rect()
            self.screen.blit(self.text_insert_coin, ((800 - rect.w)//2, 560))
            pg.display.update()
            

                           