import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,155,0)
grey = (155, 155, 155)

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption ('NotTRONtron')

clock = pygame.time.Clock()
block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def GameLoop():
    gameExit = False
    gameOver = False


    while not gameExit:
        gameDisplay.fill(blue)
        pygame.display.update()

        #Controls
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                gameExit = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                gameLoop()
