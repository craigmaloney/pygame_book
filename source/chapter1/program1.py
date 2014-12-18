#!/usr/bin/env python

import sys
import pygame

SCREENRECT = pygame.locals.Rect(0, 0, 800, 600)

def main():
    pygame.display.set_mode(SCREENRECT.size)

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
