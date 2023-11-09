import pygame
import threading


from algorithm import astar, bfs, dfs
from entities.board import Board
from entities.grid import Grid


class Pathfinder:
    def __init__(self):
        self.board = Board(16, 16)
        self.grid = Grid(16, 16)
        self.start = None
        self.finish = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    self.board = Board(16, 16)
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
            x = max(0, min(16 - 1, x // 32))
            y = max(0, min(16 - 1, y // 32))
            self._handle_mb1(x, y)
        if pygame.mouse.get_pressed()[1]:
            x, y = pygame.mouse.get_pos()
            x = max(0, min(16 - 1, x // 32))
            y = max(0, min(16 - 1, y // 32))
            self._handle_mb3(x, y)
        if pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            x = max(0, min(16 - 1, x // 32))
            y = max(0, min(16 - 1, y // 32))
            self._handle_mb2(x, y)

    def render(self, screen):
        self.board.draw(screen)
        self.grid.draw(screen)

    def _handle_mb1(self, x, y):
        tile = self.board.tiles[y][x]
        if tile == self.start:
            self.start = None
        if tile == self.finish:
            self.finish = None
        tile.state = "wall"

    def _handle_mb3(self, x, y):
        tile = self.board.tiles[y][x]
        if self.start is None and tile != self.finish:
            self.start = tile
            self.start.state = "start"
        if self.finish is None and tile != self.start:
            self.finish = tile
            self.finish.state = "finish"

    def _handle_mb2(self, x, y):
        tile = self.board.tiles[y][x]
        if tile == self.start:
            self.start = None
        if tile == self.finish:
            self.finish = None
        tile.state = "empty"
