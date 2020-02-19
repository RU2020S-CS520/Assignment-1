import utility
import numpy as np

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def valid(maze, pos):
    if pos[0] < 0 or pos[0] >= maze.size:
        return False
    if pos[1] < 0 or pos[1] >= maze.size:
        return False
    if maze[pos] == 1:
        return False
    return True


def manhattan_cost(u, v):
    return abs(u[0] - v[0]) + abs(u[0] - v[0])


def astar(maze, start, goal):
    cost = np.full((maze.size, maze.size), maze.size * maze.size)
    tree = np.ones((maze.size, maze.size, 2))
    step = 0
    tree[goal] = (-1, -1)
    cost[start] = step;
    pq = utility.pq()
    pq.put((manhattan_cost(start, goal) + 0, start))
    while not pq.empty():
        current = pq.get()
        if cost[goal] < current[0]:
            return tree

        cur_pos = current[1]

        for dir in dirs:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if valid(maze, next_pos):
                if cost[next_pos] > step + 1:
                    cost[next_pos] = step + 1
                    pq.put((manhattan_cost(next_pos, goal) + cost[next_pos], next_pos))
                    tree[next_pos] = cur_pos

    return tree


def ada_astar(maze, start, goal, last_cost):
    cost = np.full((maze.size, maze.size), maze.size * maze.size)
    tree = np.zeros((maze.size, maze.size, 2))
    step = 0
    tree[goal] = (-1, -1)
    cost[start] = step;
    pq = utility.pq()
    pq.put((last_cost[goal] - last_cost[start] + 0, start))
    while not pq.empty():
        current = pq.get()
        if cost[goal] < current[0]:
            return tree

        cur_pos = current[1]

        for dir in dirs:
            next_pos = cur_pos + dir
            if valid(maze, next_pos):
                if cost[next_pos] > step + 1:
                    cost[next_pos] = step + 1
                    np.put((last_cost[goal] - last_cost[next_pos] + cost[next_pos], next_pos))
                    tree[next_pos] = cur_pos

    return tree
