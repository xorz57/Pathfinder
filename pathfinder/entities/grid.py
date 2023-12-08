import numpy as np

from entities.tile import Tile

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = np.empty((self.rows, self.cols), dtype=object)

        for row in range(self.rows):
            for col in range(self.cols):
                self.tiles[row][col] = Tile(row, col)

        neighbor_offsets = [
            (-1, +0),
            (+1, +0),
            (+0, -1),
            (+0, +1),
        ]

        for row in range(self.rows):
            for col in range(self.cols):
                for drow, dcol in neighbor_offsets:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < self.rows and 0 <= ncol < self.cols:
                        self.tiles[row][col].neighbors.append(self.tiles[nrow][ncol])
