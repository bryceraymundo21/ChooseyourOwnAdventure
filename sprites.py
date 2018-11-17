#sprite classes for game

import pygame as pg 
from pygame.sprite import Sprite
import random
from settings import *

class MainStory(Sprite):
   def __init__(self):
        Sprite.__init__(self)
        Sprite.__init__(self)
        self.image = pg.Surface((600,360))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/3.7
        self.rect.y = 30

class LeftChoice(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 1.5)  

class MiddleChoice(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.5)

class RightChoice(Sprite):
       def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((BOX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 1.5, HEIGHT / 1.5)