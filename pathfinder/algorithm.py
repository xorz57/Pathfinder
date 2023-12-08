import collections
import heapq
import time


def _manhattan_distance(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def _heuristic(a, b):
    return (1 + 0.001) * _manhattan_distance(a, b)


def _reconstruct_path(current):
    path = []
    while current.parent:
        current = current.parent
        path.append(current)
    return path


def astar(start, finish, delay=0.001):
    start.g = 0
    start.f = _heuristic(start, finish)
    frontier = []
    heapq.heappush(frontier, (start.f, start))
    while frontier:
        time.sleep(delay)
        current = heapq.heappop(frontier)[1]
        if current == finish:
            current.state = "path"
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.state == "visited" or neighbor.state == "wall":
                continue
            g = current.g + _manhattan_distance(current, neighbor)
            if g < neighbor.g:
                if neighbor != start and neighbor != finish:
                    neighbor.state = "frontier"
                neighbor.g = g
                neighbor.f = g + _heuristic(neighbor, finish)
                neighbor.state = "visited"
                neighbor.parent = current
                heapq.heappush(frontier, (neighbor.f, neighbor))
        if current != start and current != finish:
            current.state = "visited"
    return False


def bfs(start, finish, delay=0.001):
    frontier = collections.deque()
    frontier.append(start)
    start.state = "visited"
    while frontier:
        time.sleep(delay)
        current = frontier.popleft()
        if current == finish:
            current.state = "path"
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.state == "visited" or neighbor.state == "wall":
                continue
            frontier.append(neighbor)
            neighbor.state = "visited"
            neighbor.parent = current
            if neighbor != start and neighbor != finish:
                neighbor.state = "frontier"
        if current != start and current != finish:
            current.state = "visited"
    return False


def dfs(start, finish, delay=0.001):
    frontier = collections.deque()
    frontier.append(start)
    start.state = "visited"
    while frontier:
        time.sleep(delay)
        current = frontier.pop()
        if current == finish:
            current.state = "path"
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.state == "visited" or neighbor.state == "wall":
                continue
            frontier.append(neighbor)
            neighbor.state = "visited"
            neighbor.parent = current
            if neighbor != start and neighbor != finish:
                neighbor.state = "frontier"
        if current != start and current != finish:
            current.state = "visited"
    return False
