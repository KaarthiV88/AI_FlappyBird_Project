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

