#!/usr/bin/env python
from time import sleep
import sys
import pygame
from pygame.locals import Rect

SCREENRECT = Rect(0, 0, 800, 600)
BACKGROUND_COLOR = (116, 65, 80)
LINE_COLOR = (234, 232, 211)
WIDTH = 5

def main():
    surface = pygame.display.set_mode(SCREENRECT.size)
    pygame.display.set_caption('Hi')

    surface.fill(BACKGROUND_COLOR)

    # Draw the H
    pygame.draw.line(surface, LINE_COLOR, (60, 60), (60, 120), WIDTH)
    pygame.draw.line(surface, LINE_COLOR, (100, 60), (100, 120), WIDTH)
    pygame.draw.line(surface, LINE_COLOR, (60, 90), (100, 80), WIDTH)

    # Draw the I
    pygame.draw.line(surface, LINE_COLOR, (120, 60), (120, 120), WIDTH)

    # Draw the exclamation point
    pygame.draw.line(surface, LINE_COLOR, (140, 60), (140, 110), WIDTH)
    pygame.draw.line(surface, LINE_COLOR, (140, 115), (140, 120), WIDTH)

    pygame.display.update()
    sleep(5)

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
