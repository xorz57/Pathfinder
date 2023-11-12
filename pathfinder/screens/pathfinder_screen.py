import pygame
import threading

from algorithm import astar, bfs, dfs
from config import GRID_ROWS, GRID_COLS, TILE_W, TILE_H
from entities.grid import Grid


class PathfinderScreen:
    def __init__(self):
        self.grid = Grid(GRID_ROWS, GRID_COLS)
        self.algorithm = astar
        self.start = None
        self.finish = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    self.grid = Grid(GRID_ROWS, GRID_COLS)
                    self.start = None
                    self.finish = None
                case pygame.K_SPACE:
                    if self.start != None and self.finish != None:
                        t = threading.Thread(
                            target=self.algorithm, args=(self.start, self.finish)
                        )
                        t.daemon = True
                        t.start()

    def update(self):
        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_1]:
            x, y = pygame.mouse.get_pos()
            self._handle_lmb(x, y)
        if pygame.mouse.get_pressed()[1] or pygame.key.get_pressed()[pygame.K_2]:
            x, y = pygame.mouse.get_pos()
            self._handle_mmb(x, y)
        if pygame.mouse.get_pressed()[2] or pygame.key.get_pressed()[pygame.K_3]:
            x, y = pygame.mouse.get_pos()
            self._handle_rmb(x, y)

    def render(self, screen):
        # Draw tiles
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                tile = self.grid.tiles[row][col]
                rect = (tile.col * TILE_W, tile.row * TILE_H, TILE_W, TILE_H)
                match tile.state:
                    case "empty":
                        pygame.draw.rect(screen, (238, 238, 238), rect)
                    case "wall":
                        pygame.draw.rect(screen, (49, 49, 49), rect)
                    case "path":
                        pygame.draw.rect(screen, (33, 85, 205), rect)
                    case "visited":
                        pygame.draw.rect(screen, (10, 161, 221), rect)
                    case "frontier":
                        pygame.draw.rect(screen, (121, 218, 232), rect)
                    case "start":
                        pygame.draw.rect(screen, (33, 85, 205), rect)
                    case "finish":
                        pygame.draw.rect(screen, (33, 85, 205), rect)
                    case _:
                        pygame.draw.rect(screen, (221, 17, 85), rect)
        # Draw horizontal lines
        for row in range(self.grid.rows):
            color = (82, 82, 82)
            start_pos = (0, row * TILE_H)
            end_pos = (self.grid.cols * TILE_W, row * TILE_H)
            pygame.draw.line(screen, color, start_pos, end_pos)
        # Draw vertical lines
        for col in range(self.grid.cols):
            color = (82, 82, 82)
            start_pos = (col * TILE_W, 0)
            end_pos = (col * TILE_W, self.grid.rows * TILE_H)
            pygame.draw.line(screen, color, start_pos, end_pos)

    def _clamp(self, value, minimum, maximum):
        return max(minimum, min(maximum, value))

    def _handle_lmb(self, x, y):
        row = self._clamp(y // TILE_H, 0, GRID_ROWS - 1)
        col = self._clamp(x // TILE_W, 0, GRID_COLS - 1)
        tile = self.grid.tiles[row][col]
        match tile.state:
            case "empty":
                tile.state = "wall"
            case "start":
                self.start = None
                tile.state = "wall"
            case "finish":
                self.finish = None
                tile.state = "wall"

    def _handle_mmb(self, x, y):
        row = self._clamp(y // TILE_H, 0, GRID_ROWS - 1)
        col = self._clamp(x // TILE_W, 0, GRID_COLS - 1)
        tile = self.grid.tiles[row][col]
        if tile.state != "finish" and self.start is None:
            self.start = tile
            self.start.state = "start"
        if tile.state != "start" and self.finish is None:
            self.finish = tile
            self.finish.state = "finish"

    def _handle_rmb(self, x, y):
        row = self._clamp(y // TILE_H, 0, GRID_ROWS - 1)
        col = self._clamp(x // TILE_W, 0, GRID_COLS - 1)
        tile = self.grid.tiles[row][col]
        match tile.state:
            case "wall":
                tile.state = "empty"
            case "start":
                self.start = None
                tile.state = "empty"
            case "finish":
                self.finish = None
                tile.state = "empty"
