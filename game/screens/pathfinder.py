import pygame
import threading

from config import BOARD_ROWS, BOARD_COLS, TILE_W, TILE_H
from algorithm import astar, bfs, dfs
from entities.board import Board
from entities.grid import Grid


class Pathfinder:
    def __init__(self):
        self.board = Board(BOARD_ROWS, BOARD_COLS)
        self.grid = Grid(BOARD_ROWS, BOARD_COLS)
        self.start = None
        self.finish = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    self.board = Board(BOARD_ROWS, BOARD_COLS)
                    self.start = None
                    self.finish = None
                case pygame.K_SPACE:
                    if self.start != None and self.finish != None:
                        t = threading.Thread(
                            target=astar, args=(self.start, self.finish)
                        )
                        t.daemon = True
                        t.start()

    def update(self):
        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_1]:
            x, y = pygame.mouse.get_pos()
            x = self._clamp(x // TILE_W, 0, BOARD_COLS - 1)
            y = self._clamp(y // TILE_H, 0, BOARD_ROWS - 1)
            self._handle_lmb(x, y)
        if pygame.mouse.get_pressed()[1] or pygame.key.get_pressed()[pygame.K_2]:
            x, y = pygame.mouse.get_pos()
            x = self._clamp(x // TILE_W, 0, BOARD_COLS - 1)
            y = self._clamp(y // TILE_H, 0, BOARD_ROWS - 1)
            self._handle_mmb(x, y)
        if pygame.mouse.get_pressed()[2] or pygame.key.get_pressed()[pygame.K_3]:
            x, y = pygame.mouse.get_pos()
            x = self._clamp(x // TILE_W, 0, BOARD_COLS - 1)
            y = self._clamp(y // TILE_H, 0, BOARD_ROWS - 1)
            self._handle_rmb(x, y)

    def render(self, screen):
        self.board.draw(screen)
        self.grid.draw(screen)

    def _clamp(self, value, minimum, maximum):
        return max(minimum, min(maximum, value))

    def _handle_lmb(self, x, y):
        tile = self.board.tiles[y][x]
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
        tile = self.board.tiles[y][x]
        if tile.state != "finish" and self.start is None:
            self.start = tile
            self.start.state = "start"
        if tile.state != "start" and self.finish is None:
            self.finish = tile
            self.finish.state = "finish"

    def _handle_rmb(self, x, y):
        tile = self.board.tiles[y][x]
        match tile.state:
            case "wall":
                tile.state = "empty"
            case "start":
                self.start = None
                tile.state = "empty"
            case "finish":
                self.finish = None
                tile.state = "empty"
