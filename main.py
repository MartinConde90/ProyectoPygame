import pygame as pg
from pygame.locals import *
import sys , os
from juego import *



class Game:
    
    def __init__(self):
        
        self.juego = Juego()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.juego.start_screen()