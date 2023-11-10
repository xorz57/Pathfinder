import pygame

from config import TILE_WIDTH, TILE_HEIGHT


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def draw(self, surface):
        for row in range(self.rows):
            spy = (0, row * TILE_HEIGHT)
            epy = (self.cols * TILE_WIDTH, row * TILE_HEIGHT)
            pygame.draw.line(surface, (82, 82, 82), spy, epy)
        for col in range(self.cols):
            spx = (col * TILE_WIDTH, 0)
            epx = (col * TILE_WIDTH, self.rows * TILE_HEIGHT)
            pygame.draw.line(surface, (82, 82, 82), spx, epx)
