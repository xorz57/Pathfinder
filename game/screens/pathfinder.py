import pygame
import threading


from config import BOARD_ROWS, BOARD_COLS, TILE_WIDTH, TILE_HEIGHT
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
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            x = max(0, min(BOARD_COLS - 1, x // TILE_WIDTH))
            y = max(0, min(BOARD_ROWS - 1, y // TILE_HEIGHT))
            self._handle_lmb(x, y)
        if pygame.mouse.get_pressed()[1]:
            x, y = pygame.mouse.get_pos()
            x = max(0, min(BOARD_COLS - 1, x // TILE_WIDTH))
            y = max(0, min(BOARD_ROWS - 1, y // TILE_HEIGHT))
            self._handle_mmb(x, y)
        if pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            x = max(0, min(BOARD_COLS - 1, x // TILE_WIDTH))
            y = max(0, min(BOARD_ROWS - 1, y // TILE_HEIGHT))
            self._handle_rmb(x, y)

    def render(self, screen):
        self.board.draw(screen)
        self.grid.draw(screen)

    def _handle_lmb(self, x, y):
        tile = self.board.tiles[y][x]
        if tile == self.start:
            self.start = None
        if tile == self.finish:
            self.finish = None
        tile.state = "wall"

    def _handle_mmb(self, x, y):
        tile = self.board.tiles[y][x]
        if self.start is None and tile != self.finish:
            self.start = tile
            self.start.state = "start"
        if self.finish is None and tile != self.start:
            self.finish = tile
            self.finish.state = "finish"

    def _handle_rmb(self, x, y):
        tile = self.board.tiles[y][x]
        if tile == self.start:
            self.start = None
        if tile == self.finish:
            self.finish = None
        tile.state = "empty"
