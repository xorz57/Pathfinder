import pygame

from config import TILE_W, TILE_H


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def draw(self, surface):
        for row in range(self.rows):
            spy = (0, row * TILE_H)
            epy = (self.cols * TILE_W, row * TILE_H)
            pygame.draw.line(surface, (82, 82, 82), spy, epy)
        for col in range(self.cols):
            spx = (col * TILE_W, 0)
            epx = (col * TILE_W, self.rows * TILE_H)
            pygame.draw.line(surface, (82, 82, 82), spx, epx)
