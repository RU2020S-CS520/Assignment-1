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


def manhattan_heuristics(maze, goal):
    heuristics = np.zeros((maze.shape[0], maze.shape[0]))
    for col in range(heuristics.shape[0]):
        for row in range(heuristics.shape[0]):
            heuristics[col, row] = manhattan_cost((col, row), goal)
    return heuristics

def manhattan_cost(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])



def decode_path(tree, start, goal, decode_mode=0):
    goal_last = (tree[goal][0], tree[goal][1])
    if goal_last != (-1, -1):
        cur = goal
        path = []
        if decode_mode == 0:
            while cur != start:
                path = [cur] + path
                cur = (tree[cur][0], tree[cur][1])
            path = [start] + path
        elif decode_mode == 1:
            while cur != start:
                path = path + [cur]
                cur = (tree[cur][0], tree[cur][1])
            path = path + [start]
    else:
        path = [goal_last]

    return path


def astar(maze, start, goal, decode_mode=0, priority=1):
    if decode_mode == 1:
        temp = start
        start = goal
        goal = temp

    heuristics = manhattan_heuristics(maze, goal)
    cost = np.full((maze.shape[0], maze.shape[0]), maze.shape[0] * maze.shape[0])
    closed_list = []
    tree = np.zeros((maze.shape[0], maze.shape[0], 2), dtype=np.int16)
    tree[goal] = (-1, -1)
    cost[start] = 0
    pq = utility.PriorityQueue(priority)
    pq.put(heuristics[start], 0, start)
    while not pq.empty():

        cur_pos = pq.get()
        if cost[goal] <= cost[cur_pos] + heuristics[cur_pos]:
            closed_list = closed_list + [goal]
            break

        closed_list = closed_list + [cur_pos]

        for dir in dirs:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if valid(maze, next_pos):
                if cost[next_pos] > cost[cur_pos] + 1:
                    if cost[next_pos] != maze.shape[0] * maze.shape[0]:
                        pq.remove(next_pos)
                    cost[next_pos] = cost[cur_pos] + 1
                    pq.put(heuristics[next_pos], cost[next_pos], next_pos)
                    tree[next_pos] = cur_pos

    path = decode_path(tree, start, goal, decode_mode)

    expanded = len(closed_list)

    for node in closed_list:
        heuristics[node] = max(cost[goal] - cost[node], manhattan_cost(goal, node))

    return path, heuristics, expanded, closed_list


def ada_astar(maze, start, goal, heuristics, decode_mode=0, priority=1):
    if decode_mode == 1:
        temp = start
        start = goal
        goal = temp

    if heuristics is None:
        return astar(maze, start, goal, decode_mode)


    cost = np.full((maze.shape[0], maze.shape[0]), maze.shape[0] * maze.shape[0])
    closed_list = []
    tree = np.zeros((maze.shape[0], maze.shape[0], 2), dtype=np.int16)
    tree[goal] = (-1, -1)
    cost[start] = 0
    pq = utility.PriorityQueue(priority)
    pq.put(heuristics[start], 0, start)

    while not pq.empty():
        cur_pos = pq.get()
        if cost[goal] <= cost[cur_pos] + heuristics[cur_pos]:
            closed_list = closed_list + [goal]
            break

        closed_list = closed_list + [cur_pos]

        for dir in dirs:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if valid(maze, next_pos):
                if cost[next_pos] > cost[cur_pos] + 1:
                    if cost[next_pos] != maze.shape[0] * maze.shape[0]:
                        pq.remove(next_pos)

                    cost[next_pos] = cost[cur_pos] + 1

                    # if heuristics[next_pos] > manhattan_cost(goal, next_pos):
                    #     print(heuristics[next_pos], manhattan_cost(goal, next_pos))

                    pq.put(heuristics[next_pos], cost[next_pos], next_pos)
                    tree[next_pos] = cur_pos

        path = decode_path(tree, start, goal, decode_mode)

    expanded = len(closed_list)

    for node in closed_list:
        heuristics[node] = max(cost[goal] - cost[node], heuristics[node])

    return path, heuristics, expanded, closed_list


if __name__ == '__main__':
    a = [1, 2]
    print(a.count())
    print(a + [3])
