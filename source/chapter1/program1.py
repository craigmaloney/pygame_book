#!/usr/bin/env python
import sys
import pygame
from pygame.locals import Rect

SCREENRECT = Rect(0, 0, 800, 600)


def main():
    pygame.display.set_mode(SCREENRECT.size)

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()
