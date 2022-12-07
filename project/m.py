import pygame
import sys
from board import *


pygame.init()
pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
