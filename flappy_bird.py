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
    
    
class Pipe:
    Gap = 200
    velocity = 5
    
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100
        
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG
        
        self.passThru = False
        self.setHeight()
        
    def getHeight(self):
        return self.height
    
    def setHeight(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.Gap
        
    def move(self):
        self.x -= self.velocity
        
    def draw(self, window):
        window.blit(self.PIPE_TOP, (self.x, self.top))
        window.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        
    def collision(self, Bird):
        birdMask = Bird.get_mask()
        topMask = pygame.mask.from_surface(self.PIPE_TOP)
        bottomMask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        topOffset = (self.x - Bird.x, self.top - round(Bird.y))
        bottomOffset = (self.x, Bird.x, self.bottom - round(Bird.y))
        
        b_point = birdMask.overlap(bottomMask, bottomOffset)
        t_point = birdMask.overlap(topMask, topOffset)
        
        if(t_point or b_point):
            return True       
        else:
            return False
        
        
class Base:
    velocity = 5
    width = GROUND_IMG.get_width()
    IMG = GROUND_IMG
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width
        
    def move(self):
        self.x1 -= self.velocity
        self.x2 -= self.velocity

        if(self.x1 + self.width < 0):
            self.x1 = self.x2 + self.width
        
        if(self.x2 + self.width < 0):
            self.x2 = self.x1 + self.width
            
    def draw(self, window):
        window.blit(self.IMG, (self.x1, self.y))
        window.blit(self.IMG, (self.x2, self.y))

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
