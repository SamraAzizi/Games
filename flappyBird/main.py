import random
import sys
import pygame
import pygame.locals import *

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/bird.png'
BACKGROUND = 'gallery/background.png'
PIPE = 'gallery/pipe.png'



if __name__ == "__main__":
    #this will be the main point from  where our game will start 
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display,set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/0.png')
    )

