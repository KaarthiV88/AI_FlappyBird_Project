import pygame
import neat
import time 
import os 
import random

windowWidth = 600
windowHeight = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "bird3.png")))] 
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "FBpipe.png")))
GROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "FBground.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.pag.join("FB_Imgs", "FBbg.png")))

class Bird:
    IMGS = BIRD_IMGS
    maxRotation = 25
    rotationVelocity = 20
    aniTime = 3.5
    
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

