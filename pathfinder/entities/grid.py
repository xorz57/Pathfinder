import pygame

from config import TILE_W, TILE_H
from entities.tile import Tile

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = [
            [Tile(row, col) for row in range(self.cols)] for col in range(self.rows)
        ]

        neighbor_offsets = [
            (+0, -1),
            (+1, +0),
            (+0, +1),
            (-1, +0),
        ]

        for row in range(self.rows):
            for col in range(self.cols):
                for dx, dy in neighbor_offsets:
                    nrow, ncol = row + dx, col + dy
                    if 0 <= nrow < self.rows and 0 <= ncol < self.cols:
                        self.tiles[row][col].neighbors.append(self.tiles[nrow][ncol])

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                self.tiles[row][col].draw(surface)
        for row in range(self.rows):
            spy = (0, row * TILE_H)
            epy = (self.cols * TILE_W, row * TILE_H)
            pygame.draw.line(surface, (82, 82, 82), spy, epy)
        for col in range(self.cols):
            spx = (col * TILE_W, 0)
            epx = (col * TILE_W, self.rows * TILE_H)
            pygame.draw.line(surface, (82, 82, 82), spx, epx)
