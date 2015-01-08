#!/usr/bin/env python

import sys
import pygame
from pygame.locals import Rect

SCREENRECT = Rect(0, 0, 800, 600)
BACKGROUND = (0, 0, 255)
LINE = (255, 120, 0)
WIDTH = 5

def main():
    surface = pygame.display.set_mode(SCREENRECT.size)
    pygame.display.set_caption('Hi')

    surface.fill(BACKGROUND)
    pygame.draw.line(surface, LINE, (60, 60), (60, 120), WIDTH)
    pygame.draw.line(surface, LINE, (100, 60), (100, 120), WIDTH)
    pygame.draw.line(surface, LINE, (60, 90), (100, 80), WIDTH)

    pygame.draw.line(surface, LINE, (120, 60), (120, 120), WIDTH)

    pygame.draw.line(surface, LINE, (140, 60), (140, 110), WIDTH)
    pygame.draw.line(surface, LINE, (140, 115), (140, 120), WIDTH)
    pygame.display.update()
    while True:
        pass

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
