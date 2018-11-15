#this file was created by bryce raymundo
'''sources https://goo.gl/v9tpzL  

https://bit.ly/2zZNE39
'''
import pygame as pg 
import random
from settings import *
from sprites import *
import time


class Game:
    def __init__(self):
        #init game window
        #init pygame and create window
        pg.init()
        pg.font.init()
        #init sound mixer
        pg.mixer.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        # self.textScreen =pg.surface.Surface((WIDTH,HEIGHT))
        # self.textScreen.blit(self.screen, (WIDTH,HEIGHT))
        pg.display.set_caption("Choose adventure")
        self.clock = pg.time.Clock()
        self.running = True
        self.roomNumber = 0
        self.options = "start"
        self.comicSans = pg.font.SysFont('comicsans', 300)
        self.middleBox = "hi"
        self.leftBox = ""
        self.rightBox = ""
    def new(self):
        
        #add all sprites to the group
        self.all_sprites = pg.sprite.Group()
        self.middleChoice = MiddleChoice()
        self.leftChoice = LeftChoice()
        self.rightChoice = RightChoice()
        self.all_sprites.add(self.middleChoice,self.leftChoice,self.rightChoice)
        
        #gets the size of the middle choice sprite
        self.middleRect = self.middleChoice.rect
        self.rightRect = self.rightChoice.rect
        self.leftRect = self.leftChoice.rect
        #call the run method
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()

            
    def events(self):
        
        #keeps looping the game until running is false
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            #detects if the mouse clicked on the text box
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.roomNumber == 0:
                    if self.middleRect.collidepoint(x, y):
                        print('clicked on middle box')
                    if self.rightRect.collidepoint(x,y):
                        print('clicked on right box')
                    if self.leftRect.collidepoint(x,y):
                        print('clicked on left box')
                if self.roomNumber == 1:
                    if self.middleRect.collidepoint(x, y):
                        print('clicked on middle box')
                    if self.rightRect.collidepoint(x,y):
                        print('clicked on right box')
                    if self.leftRect.collidepoint(x,y):
                        print('clicked on left box')
                if self.roomNumber == 2:
                    if self.middleRect.collidepoint(x, y):
                        print('clicked on middle box')
                    if self.rightRect.collidepoint(x,y):
                        print('clicked on right box')
                    if self.leftRect.collidepoint(x,y):
                        print('clicked on left box')
                if self.roomNumber == 3:
                    if self.middleRect.collidepoint(x, y):
                        print('clicked on middle box')
                    if self.rightRect.collidepoint(x,y):
                        print('clicked on right box')
                    if self.leftRect.collidepoint(x,y):
                        print('clicked on left box')
    #draw fills the canvas with black
    def draw(self):
        # self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        #apply text to the screen
        middleText = self.comicSans.render(self.middleBox, 1, WHITE)
        self.screen.blit(middleText, (self.leftChoice.rect.left, self.leftChoice.rect.top))
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
g.show_go_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()