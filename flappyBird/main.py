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
        pygame.image.load('gallery/0.png').convert_alpha(),
        pygame.image.load('gallery/1.png').convert_alpha(),
        pygame.image.load('gallery/2.png').convert_alpha(),
        pygame.image.load('gallery/3.png').convert_alpha(),
        pygame.image.load('gallery/4.png').convert_alpha(),
        pygame.image.load('gallery/5.png').convert_alpha(),
        pygame.image.load('gallery/6.png').convert_alpha(),
        pygame.image.load('gallery/7.png').convert_alpha(),
        pygame.image.load('gallery/8.png').convert_alpha(),
        pygame.image.load('gallery/9.png').convert_alpha(),

    )

    GAME_SPRITES['message'] = pygame.image.load('gallery/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/message.png').convert_alpha()
    GAME_SPRITES['pipe'] = pygame.image.load('gallery/message.png').convert_alpha()

