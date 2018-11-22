#this file was created by bryce raymundo
'''sources https://goo.gl/v9tpzL  

https://bit.ly/2zZNE39
https://bit.ly/2FoTOzK
'''
import pygame as pg 
import random
from settings import *
from sprites import *
import time
import sys

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
        pg.display.set_caption("Choose adventure")
        self.clock = pg.time.Clock()
        self.running = True
        self.roomNumber = 0
        self.options = "start"
        self.comicSans = pg.font.SysFont('comicsans', 30)
        #initializes variables for each line of text
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

        self.mainBoxL1 = "first Line"
        self.mainBoxL2 = "second Line"
        self.mainBoxL3 = "third line"
        self.mainBoxL4 = "fourth Line"
        self.mainBoxL5 = "fifth Line"
        self.mainBoxL6 = "sixth Line"
        self.mainBoxL7 = "seventh Line"
  
    def new(self):
        
        #add all sprites to the group
        self.all_sprites = pg.sprite.Group()
        self.middleChoice = MiddleChoice()
        self.leftChoice = LeftChoice()
        self.rightChoice = RightChoice()
        self.mainStory = MainStory()
        self.all_sprites.add(self.middleChoice,self.leftChoice,self.rightChoice,self.mainStory)
        
        #gets the size of the text boxes
        self.middleRect = self.middleChoice.rect
        self.rightRect = self.rightChoice.rect
        self.leftRect = self.leftChoice.rect
        self.mainRect = self.mainStory.rect

        #call the run method
        self.run()
    def run(self):
        #runs while playing is true
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
            #detects if the mouse clicked on a text box
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.roomNumber == 0:
                    if self.middleRect.collidepoint(x, y):
                        self.mainBoxL2=self.mainBoxL1
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
        middleTextL3 = self.comicSans.render(self.middleBoxL3, 1, BLACK)
        middleTextL2 = self.comicSans.render(self.middleBoxL2, 1, BLACK)

        leftTextL1 = self.comicSans.render(self.leftBoxL1, 1, BLACK)
        leftTextL2 = self.comicSans.render(self.leftBoxL2, 1, BLACK)
        leftTextL3 = self.comicSans.render(self.leftBoxL3, 1, BLACK)

        rightTextL1 = self.comicSans.render(self.rightBoxL1, 1, BLACK)
        rightTextL2 = self.comicSans.render(self.rightBoxL2, 1, BLACK)
        rightTextL3 = self.comicSans.render(self.rightBoxL3, 1, BLACK)

        self.mainTextL1 = self.comicSans.render(self.mainBoxL1, 1, BLACK)
        mainTextL2 = self.comicSans.render(self.mainBoxL2, 1, BLACK)
        mainTextL3 = self.comicSans.render(self.mainBoxL3, 1, BLACK)
        mainTextL4 = self.comicSans.render(self.mainBoxL4, 1, BLACK)
        mainTextL5 = self.comicSans.render(self.mainBoxL5, 1, BLACK)
        mainTextL6 = self.comicSans.render(self.mainBoxL6, 1, BLACK)
        mainTextL7 = self.comicSans.render(self.mainBoxL7, 1, BLACK)

        self.screen.blit(leftTextL1, (self.leftRect.left+10, self.leftRect.top+10))
        self.screen.blit(leftTextL2, (self.leftRect.left+10, self.leftRect.top+30))
        self.screen.blit(leftTextL3, (self.leftRect.left+10, self.leftRect.top+50))

        self.screen.blit(middleTextL1, (self.middleRect.left+10, self.middleRect.top+10))
        self.screen.blit(middleTextL2, (self.middleRect.left+10, self.middleRect.top+30))
        self.screen.blit(middleTextL3, (self.middleRect.left+10, self.middleRect.top+50))

        self.screen.blit(rightTextL1, (self.rightRect.left+10, self.rightRect.top+10))
        self.screen.blit(rightTextL2, (self.rightRect.left+10, self.rightRect.top+30))
        self.screen.blit(rightTextL3, (self.rightRect.left+10, self.rightRect.top+50))

        #self.display_text_animation(self.mainBoxL1,self.mainTextL1,10,330)
        self.screen.blit(self.mainTextL1, (self.mainRect.left+10, self.mainRect.top+330))
        self.screen.blit(mainTextL2, (self.mainRect.left+10, self.mainRect.top+305))
        self.screen.blit(mainTextL3, (self.mainRect.left+10, self.mainRect.top+280))
        self.screen.blit(mainTextL4, (self.mainRect.left+10, self.mainRect.top+255))
        self.screen.blit(mainTextL5, (self.mainRect.left+10, self.mainRect.top+230))
        self.screen.blit(mainTextL6, (self.mainRect.left+10, self.mainRect.top+205))
        self.screen.blit(mainTextL7, (self.mainRect.left+10, self.mainRect.top+180))

    #attempt at making the text appear one character at at time
    def display_text_animation(self,message,text,xVal,yVal):
        text = ''
        self.its=0
        for i in range(len(message)):
            text += message[i]
            # text_surface = font.render(text, True, BLACK)
            # text_rect = text_surface.get_rect()
            # text_rect.center = (xVal, yVal)
            self.screen.blit(self.mainTextL1, (self.mainRect.left + xVal, self.mainRect.top + yVal))
            # pygame.display.update()
            # pygame.time.wait(100)
            print(self.its)
            self.its+=1
            pg.time.wait(1000)
    def draw(self):
        self.all_sprites.draw(self.screen)
        #apply text to the screen
        self.addText()
        pg.display.flip()
    def draw_main_text(self):
        pass
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