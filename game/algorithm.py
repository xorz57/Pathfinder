import collections
import heapq
import math
import time


def _heuristic(a, b):
    return math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2)


def _reconstruct_path(current):
    path = []
    while current.parent:
        current = current.parent
        path.append(current)
    return path


def astar(start, finish, delay=0.025):
    start.g = 0
    start.f = 0 + _heuristic(start, finish)
    frontier = []
    heapq.heappush(frontier, (start.f, start))
    while frontier:
        time.sleep(delay)
        current = heapq.heappop(frontier)[1]
        if current == finish:
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.visited or neighbor.state == "wall":
                continue
            g = current.g + 1
            if g < neighbor.g:
                if neighbor != start and neighbor != finish:
                    neighbor.state = "frontier"
                neighbor.g = g
                neighbor.f = g + _heuristic(neighbor, finish)
                neighbor.visited = True
                neighbor.parent = current
                heapq.heappush(frontier, (neighbor.f, neighbor))
        if current != start and current != finish:
            current.state = "visited"
    return False


def bfs(start, finish, delay=0.025):
    frontier = collections.deque()
    frontier.append(start)
    start.visited = True
    while frontier:
        time.sleep(delay)
        current = frontier.popleft()
        if current == finish:
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.visited or neighbor.state == "wall":
                continue
            frontier.append(neighbor)
            neighbor.visited = True
            neighbor.parent = current
            if neighbor != start and neighbor != finish:
                neighbor.state = "frontier"
        if current != start and current != finish:
            current.state = "visited"
    return False


def dfs(start, finish, delay=0.025):
    frontier = collections.deque()
    frontier.append(start)
    start.visited = True
    while frontier:
        time.sleep(delay)
        current = frontier.pop()
        if current == finish:
            path = _reconstruct_path(current)
            for tile in path:
                if tile is not None and tile != start:
                    tile.state = "path"
            return True
        for neighbor in current.neighbors:
            if neighbor.visited or neighbor.state == "wall":
                continue
            frontier.append(neighbor)
            neighbor.visited = True
            neighbor.parent = current
            if neighbor != start and neighbor != finish:
                neighbor.state = "frontier"
        if current != start and current != finish:
            current.state = "visited"
    return False
