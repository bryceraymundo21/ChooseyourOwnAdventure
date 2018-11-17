#sprite classes for game

import pygame as pg 
from pygame.sprite import Sprite
import random
from settings import *



  
class LeftChoice(Sprite):
       def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 1.5)
        self.vx = 0
        self.vy = 0

class MiddleChoice(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.5)
        self.vx = 0
        self.vy = 0
       

class RightChoice(Sprite):
       def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 1.5, HEIGHT / 1.5)
        self.vx = 0
        self.vy = 0
