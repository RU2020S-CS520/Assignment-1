import utility
import numpy as np

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def valid(maze, pos):
    if pos[0] < 0 or pos[0] >= maze.shape[0]:
        return False
    if pos[1] < 0 or pos[1] >= maze.shape[0]:
        return False
    if maze[pos] == 1:
        return False
    return True


def manhattan_cost(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


def decode_path(tree, start, goal, decode_mode):
    if tree[goal][0] != -1 and tree[goal][1] != -1:
        cur = goal
        path = []
        while cur != start:
            if decode_mode == 0:
                path = [cur] + path
            elif decode_mode == 1:
                path = path + [cur]
            cur = (tree[cur][0], tree[cur][1])
        path = [start] + path
    else:
        path = [start]

    return path


def astar(maze, start, goal, decode_mode=0):
    cost = np.full((maze.shape[0], maze.shape[0]), maze.shape[0] * maze.shape[0])
    tree = np.zeros((maze.shape[0], maze.shape[0], 2), dtype=np.int16)
    tree[goal] = (-1, -1)
    cost[start] = 0
    pq = utility.PriorityQueue(0)
    pq.put(manhattan_cost(start, goal), 0, start)
    while not pq.empty():
        cur_pos = pq.get()
        if cost[goal] < cost[cur_pos] + manhattan_cost(start, goal):
            break

        for dir in dirs:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if valid(maze, next_pos):
                if cost[next_pos] > cost[cur_pos] + 1:
                    cost[next_pos] = cost[cur_pos] + 1
                    pq.put(manhattan_cost(next_pos, goal), cost[next_pos], next_pos)
                    tree[next_pos] = cur_pos

    path = decode_path(tree, start, goal, decode_mode)

    return path, cost


def ada_astar(maze, start, goal, last_cost, decode_mode=0):
    if last_cost is None:
        return astar(maze, start, goal, decode_mode)

    cost = np.full((maze.shape[0], maze.shape[0]), maze.shape[0] * maze.shape[0])
    tree = np.zeros((maze.shape[0], maze.shape[0], 2), dtype=np.int16)
    tree[goal] = (-1, -1)
    cost[start] = 0
    pq = utility.PriorityQueue(0)
    pq.put(last_cost[goal] - last_cost[start], 0, start)
    while not pq.empty():
        cur_pos = pq.get()

        if cost[goal] < cost[cur_pos] + last_cost[goal] - last_cost[cur_pos]:
            break

        for dir in dirs:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if valid(maze, next_pos):
                if cost[next_pos] > cost[cur_pos] + 1:
                    cost[next_pos] = cost[cur_pos] + 1
                    pq.put(last_cost[goal] - last_cost[next_pos], cost[next_pos], next_pos)
                    tree[next_pos] = cur_pos

        path = decode_path(tree, start, goal, decode_mode)

    return path, cost


if __name__ == '__main__':
    kk = np.zeros((3, 3))
    kd = np.ones((3, 3))
    tp = []
    tp = [(1, 2)] + tp
    print(tp)
    kk[2, 2] = 1
    print(kd.shape[0])
