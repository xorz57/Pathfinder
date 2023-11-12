import math


class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.f = math.inf
        self.g = math.inf
        self.neighbors = []
        self.parent = None
        self.state = "empty"

    def __lt__(self, other):
        return self.f < getattr(other, "f", other)
