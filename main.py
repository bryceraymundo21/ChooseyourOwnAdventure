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
        self.comicSans = pg.font.SysFont('comicsans', 30)
        self.leftBoxL1 = "first Line"
        self.leftBoxL2 = "second Line"
        self.leftBoxL3 = "third Line"
        self.leftBoxL4 = "fourth Line"

        self.middleBoxL1 = "first Line"
        self.middleBoxL2 = "second Line"
        self.middleBoxL3 = "third Line"
        self.middleBoxL4 = "fourth Line"

        self.rightBoxL1 = "first Line"
        self.rightBoxL2 = "second Line"
        self.rightBoxL3 = "third Line"
        self.rightBoxL4 = "fourth Line"
    def new(self):
        
        #add all sprites to the group
        self.all_sprites = pg.sprite.Group()
        self.middleChoice = MiddleChoice()
        self.leftChoice = LeftChoice()
        self.rightChoice = RightChoice()
        self.all_sprites.add(self.middleChoice,self.leftChoice,self.rightChoice)
        
        #gets the size of the text boxes
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
    def addText(self):

        #puts the adding of text into one function
        middleTextL1 = self.comicSans.render(self.middleBoxL1, 1, BLACK)
        middleTextL2 = self.comicSans.render(self.middleBoxL2, 1, BLACK)
        middleTextL3 = self.comicSans.render(self.middleBoxL3, 1, BLACK)

        leftTextL1 = self.comicSans.render(self.leftBoxL1, 1, BLACK)
        leftTextL2 = self.comicSans.render(self.leftBoxL2, 1, BLACK)
        leftTextL3 = self.comicSans.render(self.leftBoxL3, 1, BLACK)

        rightTextL1 = self.comicSans.render(self.rightBoxL1, 1, BLACK)
        rightTextL2 = self.comicSans.render(self.rightBoxL2, 1, BLACK)
        rightTextL3 = self.comicSans.render(self.rightBoxL3, 1, BLACK)

        self.screen.blit(leftTextL1, (self.leftRect.left+10, self.leftRect.top+10))
        self.screen.blit(leftTextL2, (self.leftRect.left+10, self.leftRect.top+30))
        self.screen.blit(leftTextL3, (self.leftRect.left+10, self.leftRect.top+50))

        self.screen.blit(middleTextL1, (self.middleRect.left+10, self.middleRect.top+10))
        self.screen.blit(middleTextL2, (self.middleRect.left+10, self.middleRect.top+30))
        self.screen.blit(middleTextL3, (self.middleRect.left+10, self.middleRect.top+50))

        self.screen.blit(rightTextL1, (self.rightRect.left+10, self.rightRect.top+10))
        self.screen.blit(rightTextL2, (self.rightRect.left+10, self.rightRect.top+30))
        self.screen.blit(rightTextL3, (self.rightRect.left+10, self.rightRect.top+50))


    def draw(self):
        self.all_sprites.draw(self.screen)
        #apply text to the screen
        self.addText()
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