import pygame
import neat
import time 
import os 
import random
import math
import numpy as np

windowWidth = 800
windowHeight = 1000


BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FB_Imgs", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("FB_Imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("FB_Imgs", "bird3.png")))] 
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FB_Imgs", "FBpipe.png")))
GROUND_IMG = (pygame.image.load(os.path.join("FB_Imgs", "FBground.png")))
BG_IMG = (pygame.image.load(os.path.join("FB_Imgs", "FBbg.png")))

class Bird:
    IMGS = BIRD_IMGS
    maxRotation = 25
    rotationVelocity = 20
    aniTime = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCount = 0
        self.velocity = 0
        self.height = self.y
        self.imgCount = 0
        self.img = self.IMGS[0]
        
    def jump(self):
        self.velocity = -10
        self.tickCount = 0
        self.height = self.y
        
    def move(self):
        self.tickCount += 1
        displacement = self.velocity * self.tickCount + 0.5*3*self.tickCount**2
        
        if(displacement >= 16):
            displacement = 16
            
        if(displacement < 0):
            displacement -= 1.75
            
        self.y += displacement
        if(displacement<0 or self.y < (self.height+50)):
            if(self.tilt < self.maxRotation):
                self.tilt = self.maxRotation
                
        else:
            if(self.tilt > -90):
                self.tilt -= self.rotationVelocity
                
    
    def draw(self, win):
        self.imgCount += 1
        if(self.imgCount < self.aniTime):
            self.img = self.IMGS[0]
        elif(self.imgCount < (self.aniTime*2)):
            self.img = self.IMGS[1]
        elif(self.imgCount < (self.aniTime*3)):
            self.img = self.IMGS[2]
        elif(self.imgCount < (self.aniTime*4)):
            self.img = self.IMGS[1]
        elif(self.imgCount == ((self.aniTime*4)+1)):
            self.img = self.IMGS[0]
            self.imgCount = 0
            
        
        if(self.tilt <= -85):
            self.img = self.IMGS[1]
            self.imgCount = self.aniTime*2
            
        rotatedImages = pygame.transform.rotate(self.img, self.tilt)
        newRectangle = rotatedImages.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotatedImages, newRectangle.topleft)
        
        #blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
    


def draw_window(win, bird): 
    win.blit(BG_IMG, (-10,-10))
    bird.draw(win)
    pygame.display.update()
    
def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((windowWidth, windowHeight))
    run = True
    
    while(run == True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
        
        draw_window(window, bird)
    
    pygame.quit()
    quit()
    
main()
