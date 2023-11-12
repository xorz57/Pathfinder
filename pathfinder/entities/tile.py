import math


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
