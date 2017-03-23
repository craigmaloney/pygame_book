#!/usr/bin/env python
import sys
import pygame
from pygame.locals import (
    Rect)

SCREENRECT = Rect(0, 0, 800, 600)
BACKGROUND_COLOR = (0, 0, 0)


def main():
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(SCREENRECT.size)
    surface.fill(BACKGROUND_COLOR)
    while running:
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
    sys.exit()
