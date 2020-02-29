import search, GridWorld
from copy import deepcopy
if __name__ == '__main__':
    maze = GridWorld.Maze(5, 5)

    maze.test()
    maze2 = deepcopy(maze)

    while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
        result = search.astar(maze.get_map(), maze.start, maze.end, priority=0)

        path = result[0]
        print(result[3])
        if path[-1] == maze.start:
            print("no path")
            break
        last_cost = result[1]
        maze.vis_map(result[3])
        maze.move(path)

    while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:
        result2 = search.astar(maze2.get_map(), maze2.start, maze2.end, priority=1)

        path = result2[0]
        if path[-1] == maze2.start:
            print("no path")
            break
        last_cost = result2[1]
        print(result2[3])
        maze2.vis_map(result2[3])
        maze2.move(path)

