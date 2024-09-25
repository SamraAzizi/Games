import random
import sys
import pygame
from pygame.locals import *

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

def welcomeScreen():
    

    playerX = int(SCREENWIDTH/5)
    playerY = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2
    messageX = int(SCREENWIDTH - GAME_SPRITES['message'].get_width())/2
    messageY = int(SCREENHEIGHT * 0.13)
    baseX = 0

    while True:
        for event in pygame.event.get():
            # if users clicks on cross button close the game

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

                # if the user presses space or up key , start the game for them 







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
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image,load(PIPE).convert_alpha())
    
    #game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pyagem.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


    while True:
        welcomeScreen() # shows a welcome scrren to the users until he presses a button

        mainGame()


