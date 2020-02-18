import pygame as pg
from pygame.locals import *
import sys , os

GREEN = (38, 158, 41)
FUCSIA = (236, 52, 234)
RED = (229, 9, 9)
WHITE = (255, 255, 255)
NARANJA = (255, 131, 0)

class Texto():
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('The Quest')

        self.background_image = pg.image.load('resources/fondo/nebula2.jpg').convert()
        self.background_img = pg.image.load('resources/fondo/espacio1.jpg').convert()
        self.background_story = pg.image.load('resources/fondo/Reference2.jpg').convert()
        self.background_menu = pg.image.load('resources/fondo/unnamed.jpg').convert()
        self.background_rules = pg.image.load('resources/fondo/controls.jpg').convert()
        self.UP = pg.image.load('resources/up.png').convert_alpha()
        self.DOWN = pg.image.load('resources/down.png').convert_alpha()
        self.Planet = pg.image.load('resources/planeta/PlanetRaw.png').convert_alpha()


        self.fontGran = pg.font.Font('resources/fonts/gameover.ttf', 150)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 90) 
        self.fontC = pg.font.Font('resources/fonts/PressStart.ttf', 25)
        self.fontR = pg.font.Font('resources/fonts/text.ttf', 30)
        self.fontP = pg.font.Font('resources/fonts/PressStart.ttf', 30)
        self.fontG = pg.font.Font('resources/fonts/gameover.ttf',85)
        self.fontL = pg.font.Font('resources/fonts/text.ttf', 50)
        self.fontRanking = pg.font.Font('resources/fonts/ranking.ttf', 100)

        #self.marcador = self.fontP.render('0', True, WHITE) 
        #self.livescounter = self.fontP.render('5', True, WHITE) 

        self.text_rankings = self.fontRanking.render("BEST SCORES",True, FUCSIA)
        self.text_level = self.fontL.render(" + 150 XP" ,True, FUCSIA) 
        self.text_insert_coin = self.fontC.render("Press   Spacebar", True, FUCSIA) 
        self.text_insertCoin = self.fontR.render("-  Insert Coin  -", True, FUCSIA)    
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
        self.text_instructions = self.fontR.render("I to see instructions", True, WHITE)
        self.text_story = self.fontR.render("S  to know your story", True, WHITE)
        self.text_ranking = self.fontR.render("R to see best scores", True, WHITE)
        

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
    def run7(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/controls.ogg')
        pg.mixer.music.play()
    def run8(self):
        pg.mixer.init()
        pg.mixer.music.load('resources/sounds/gameover.mp3')
        pg.mixer.music.play()