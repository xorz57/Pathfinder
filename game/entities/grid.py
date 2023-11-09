import pygame


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def draw(self, surface):
        for row in range(self.rows):
            spy = (0, row * 32)
            epy = (self.cols * 32, row * 32)
            pygame.draw.line(surface, (82, 82, 82), spy, epy)
        for col in range(self.cols):
            spx = (col * 32, 0)
            epx = (col * 32, self.rows * 32)
            pygame.draw.line(surface, (82, 82, 82), spx, epx)
