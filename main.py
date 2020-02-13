import pygame as pg
from pygame.locals import *
import sys , os
from random import randint
from pygame import *
from Nave import *
from Asteroides import *
from explosion import *

FPS = 60
GREEN = (38, 158, 41)
FUCSIA = (236, 52, 234)
RED = (229, 9, 9)
WHITE = (255, 255, 255)
NARANJA = (255, 131, 0)
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


        self.fontGran = pg.font.Font('resources/fonts/gameover.ttf', 150)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 90) 
        self.fontC = pg.font.Font('resources/fonts/PressStart.ttf', 30)
        self.fontR = pg.font.Font('resources/fonts/text.ttf', 30)
        self.fontP = pg.font.Font('resources/fonts/PressStart.ttf', 50)
        self.fontG = pg.font.Font('resources/fonts/gameover.ttf',85)

        #self.marcador = self.fontP.render('0', True, WHITE) 
        #self.livescounter = self.fontP.render('5', True, WHITE)       
        self.text_insert_coin = self.fontC.render("Press   Spacebar", True, FUCSIA)     
        self.text_gameOver = self.fontGran.render("GAME OVER", True, RED)       
        self.text_titulo = self.font.render("THE QUEST", True, GREEN)
        self.text_win = self.fontG.render("Level Complete", True, GREEN) 
        
        self.text_historia1 = self.fontR.render("Cuaderno de bitacora: La humanidad, en el culmen de su abandono por el  ", True, NARANJA)
        self.text_historia2 = self.fontR.render("cuidado del planeta que les dio la vida, ha acabado con todos los recursos", True, NARANJA)
        self.text_historia3 = self.fontR.render("que este ofrecia. Tras decadas de guerras por controlar la", True, NARANJA)
        self.text_historia4 = self.fontR.render("poca agua potable que quedaba, un invierno nuclear ha terminado", True, NARANJA)
        self.text_historia5 = self.fontR.render("por destruir todo el ecosistema terrestre mermado ya por el cambio", True, NARANJA)
        self.text_historia6 = self.fontR.render(" climatico. En un ultimo esfuerzo, las naciones supervivientes han", True, NARANJA)
        self.text_historia7 = self.fontR.render("unido fuerzas y construido la ultima obra maestra de ingenieria humana, ", True, NARANJA)
        self.text_historia8 = self.fontR.render("una nave espacial con la capacidad de realizar viajes interestelares.", True, NARANJA)
        self.text_historia9 = self.fontR.render("Eres lo mejor que tenemos, todas nuestras esperanzas recaen en ti. ", True, NARANJA)
        self.text_historia10 = self.fontR.render("Encuentranos un nuevo hogar.", True, NARANJA)


        self.text_controlesU = self.fontR.render("Pulsa           para    subir", True, GREEN)
        self.text_controlesD = self.fontR.render("Pulsa           para    bajar", True, GREEN)
        self.text_controlesS = self.fontR.render("Manten pulsado          o          para aumentar la velocidad", True, GREEN)
        self.text_controlesE = self.fontR.render("Pulsa            para salir del juego", True, GREEN)
        self.text_return = self.fontC.render("Press   Spacebar   to   return", True, FUCSIA)
        self.text_instructions = self.fontR.render("Press I to see instructions", True, WHITE)
        self.text_story = self.fontR.render("Press S  to know your story", True, WHITE)
        
        self.player_group = pg.sprite.Group()
        self.asteroid_group = pg.sprite.Group()      
        self.all_group = pg.sprite.Group()

        self.meteorito = Meteor()
        self.asteroid_group.add(self.meteorito)
    
        self.ship = Nave(10, 300)
        self.player_group.add(self.ship)
        self.ship.lives = 2
        self.contador = 0   
        self.puntuacion = 0
        self.all_group.add(self.ship, self.asteroid_group)
        self.default_font = pg.font.Font(None, 28)

        self.meteor_max = 15
        self.meteor_creados = 0
        self.ultimo_meteor = FPS * 12
        self.nuevo_meteor = FPS// 4
        #self.run6()
        #self.run5()
        #self.run4()
        #self.run3()
        #self.run2()
        #self.run1()

        self.time = pg.time.get_ticks()/1000
        
        
        

    def run1(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/menu.mp3')
        pg.mixer.music.play()
    def run2(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/open.mp3')
        pg.mixer.music.play()
    def run3(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/back.mp3')
        pg.mixer.music.play()
    def run4(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/play.mp3')
        pg.mixer.music.play()
    def run5(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/explosion.mp3')
        pg.mixer.music.play()
    def run6(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/story.mp3')
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
                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit()
           
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
            rect = self.text_titulo.get_rect()
            self.screen.blit(self.text_titulo,((800 - rect.w)//2,100))
            rect = self.text_insert_coin.get_rect()
            self.screen.blit(self.text_insert_coin,((800 - rect.w)//2,330)) 
            self.screen.blit(self.text_instructions,(50,560))
            self.screen.blit(self.text_story,(500,560))
            self.ship.lives = 1
            
            pg.display.update()
            for event in pg.event.get():

                if event.type == KEYDOWN:
                        if event.key == K_i:
                            self.run3()
                            self.rules_screen()
                            return
               
                        if event.key == K_SPACE:                                    
                            #self.run4()        
                            self.mainloop()
                            
                            return
                
                        if event.key == K_s:
                            #self.run3()
                            #self.run6()
                            self.Story_screen()
                            return

                
                        if event.key == K_ESCAPE:
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
            self.screen.blit(self.text_controlesE,(100,400))
            self.screen.blit(self.UP,(340,300))
            self.screen.blit(self.DOWN,(270,300))
            rect = self.text_return.get_rect()
            self.screen.blit(self.text_return,((800 - rect.w)//2,560))

            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            #self.run2() 
                            #self.run1()
                            self.start_screen()
                            return
                
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()
    
    def Story_screen(self):
        while True:
            self.screen.blit(self.background_story,(0,0))
            rect = self.text_return.get_rect()
            self.screen.blit(self.text_return,((800 - rect.w)//2,560))
            self.screen.blit(self.text_historia1,(50, 25))
            self.screen.blit(self.text_historia2,(50, 75))
            self.screen.blit(self.text_historia3,(50, 125))
            self.screen.blit(self.text_historia4,(50, 175))
            self.screen.blit(self.text_historia5,(50, 225))
            self.screen.blit(self.text_historia6,(50, 275))
            self.screen.blit(self.text_historia7,(50, 325))
            self.screen.blit(self.text_historia8,(50, 375))
            self.screen.blit(self.text_historia9,(50, 425))
            self.screen.blit(self.text_historia10,(230, 475))
            
            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            #self.run2()
                            #self.run1()
                            self.start_screen()
                            return
                
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()
    
    def gameOver(self):
        while True:
            rect = self.text_gameOver.get_rect()
            self.screen.blit(self.text_gameOver, ((800 - rect.w)//2, 200))
            rect = self.text_insert_coin.get_rect()
            self.screen.blit(self.text_insert_coin, ((800 - rect.w)//2, 560))
                  
            pg.display.update()       
            for event in pg.event.get():
                    if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                self.ship = Nave(10, 300)
                                self.player_group.add(self.ship)
                                self.all_group.add(self.ship)
                                self.asteroid_group.empty()
                                self.puntuacion = 0
                                self.meteorito.kill()
                                #self.run1() 
                                self.start_screen()
                                return
                    if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pg.quit()
                                sys.exit()
   
    def mainloop(self):
        while True:

            dt = self.clock.tick(FPS)
            self.time = pg.time.get_ticks()//1000
            self.handleEvents()
        
            
            if len(self.asteroid_group) == 14:
                self.puntuacion += 5

            self.livescounter = self.fontP.render(str(self.ship.lives), True, WHITE)
            self.marcador = self.fontP.render(str(self.puntuacion), True, WHITE)
            
            if self.ship.lives > 1:
                self.colision = pg.sprite.groupcollide(self.asteroid_group, self.player_group, True, False  ) 
                for hit in self.colision:
                    expl = Explosion(hit.rect.center)
                    #self.run5()
                    self.all_group.add(expl)   
                        
                    self.contador += 1
                if self.contador > 0:              
                    self.ship.lives -= 1
            self.contador = 0

            if self.ship.lives == 1:
                self.colision = pg.sprite.groupcollide(self.player_group, self.asteroid_group, True, False)
                for hit in self.colision:
                    expl = Explosion(hit.rect.center)
                    #self.run5()
                    self.all_group.add(expl)   
                    self.contador += 1
                if self.contador > 0:              
                    self.ship.lives -= 1

            print(len(self.asteroid_group))
            self.screen.blit(self.background_img,(0,0))           
                
            self.all_group.update(dt)
            self.all_group.draw(self.screen) 

            pintados = len(self.asteroid_group)
            if pintados < self.meteor_max:
                self.nuevoMeteor(dt)

            if self.puntuacion == 500:
                rect = self.text_win.get_rect()
                self.screen.blit(self.text_win, ((800 - rect.w)//2, 200))
                

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.screen)           
            self.screen.blit(self.livescounter, (50, 10))
            self.screen.blit(self.marcador, (660, 10))

            if self.ship.lives == 0:
                
                self.gameOver()

            pg.display.flip()

            
        self.quitGame()

            


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.start_screen()