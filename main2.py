import numpy as np
import GridWorld
import search
from copy import deepcopy

if __name__ == '__main__':
    maze = GridWorld.Maze(5, 5)

    maze.test()

    maze.visualize()

    expanded1=0
    expanded2=0
    while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
        result = search.astar(maze.get_map(), maze.start, maze.end,mod=1)

        path = result[0]
        expanded_list=result[3]
        print(path)
        print(expanded_list)
        if path[-1] == maze.start:
            print("no path")
            break
        last_cost = result[1]
        print("each time")
        print(result[2])
        expanded1+=result[2]

        maze.vis_map(expanded_list)
        maze.move(path)


    print(expanded1)
