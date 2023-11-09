from entities.tile import Tile


class Board:
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
                    if 0 <= nrow < self.cols and 0 <= ncol < self.rows:
                        self.tiles[row][col].neighbors.append(self.tiles[nrow][ncol])

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                self.tiles[row][col].draw(surface)
