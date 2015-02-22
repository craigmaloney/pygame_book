#!/usr/bin/env python
from time import sleep
import sys
import pygame
from pygame.locals import Rect
from pygame.constants import (
    KEYDOWN,
    QUIT,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_q)

SCREENRECT = Rect(0, 0, 800, 600)
BACKGROUND_COLOR = (116, 65, 80)
LINE_COLOR = (234, 232, 211)
WIDTH = 5
OFFSET = 60

def main():
    surface = pygame.display.set_mode(SCREENRECT.size)
    pygame.display.set_caption('Hi')
    pygame.key.set_repeat(1, 1)
    offset_x = OFFSET 
    offset_y = OFFSET 
    running = True

    while running:

        surface.fill(BACKGROUND_COLOR)
        # Draw the H
        pygame.draw.line(surface, LINE_COLOR, (offset_x, offset_y), (offset_x, offset_y + 60), WIDTH)
        pygame.draw.line(surface, LINE_COLOR, (offset_x + 40, offset_y), (offset_x + 40, offset_y + 60), WIDTH)
        pygame.draw.line(surface, LINE_COLOR, (offset_x, offset_y + 30), (offset_x + 40, offset_y + 20), WIDTH)

        # Draw the I
        pygame.draw.line(surface, LINE_COLOR, (offset_x + 60, offset_y), (offset_x + 60, offset_y + 60), WIDTH)

        # Draw the exclamation point
        pygame.draw.line(surface, LINE_COLOR, (offset_x + 80, offset_y), (offset_x + 80, offset_y + 50), WIDTH)
        pygame.draw.line(surface, LINE_COLOR, (offset_x + 80, offset_y + 55), (offset_x + 80, offset_y + 60), WIDTH)
        
        events = pygame.event.get()
        for e in events:
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN and (e.key == K_ESCAPE or e.key == K_q):
                running = False
            if e.type == KEYDOWN and e.key == K_UP:
                offset_y -= 1
            if e.type == KEYDOWN and e.key == K_DOWN:
                offset_y += 1
            if e.type == KEYDOWN and e.key == K_LEFT:
                offset_x -= 1
            if e.type == KEYDOWN and e.key == K_RIGHT:
                offset_x += 1

        pygame.display.update()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
