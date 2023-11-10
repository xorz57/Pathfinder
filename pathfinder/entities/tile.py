import math
import pygame

from config import TILE_W, TILE_H


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = math.inf
        self.g = math.inf
        self.neighbors = []
        self.visited = False
        self.parent = None
        self.state = "empty"

    def __lt__(self, other):
        return self.f < getattr(other, "f", other)

    def draw(self, surface):
        rect = (self.x * TILE_W, self.y * TILE_H, TILE_W, TILE_H)
        match self.state:
            case "empty":
                pygame.draw.rect(surface, (238, 238, 238), rect)
            case "wall":
                pygame.draw.rect(surface, (49, 49, 49), rect)
            case "path":
                pygame.draw.rect(surface, (33, 85, 205), rect)
            case "visited":
                pygame.draw.rect(surface, (10, 161, 221), rect)
            case "frontier":
                pygame.draw.rect(surface, (121, 218, 232), rect)
            case "start":
                pygame.draw.rect(surface, (33, 85, 205), rect)
            case "finish":
                pygame.draw.rect(surface, (33, 85, 205), rect)
