import numpy as np
import GridWorld
import search
from copy import deepcopy
import matplotlib.pyplot as plt



if __name__ == '__main__':
    expanded1_all=[]
    expanded2_all=[]
    for i in range(1):

        maze = GridWorld.Maze(5, 5)
        maze.test()
        last_cost = None
        k = 0
        maze2 = deepcopy(maze)
        while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
            result2 = search.ada_astar(maze.get_map(), maze.start, maze.end, last_cost, decode_mode=0, priority=1)
            path = result2[0]
            last_cost = result2[1]

            if path[-1] == (-1, -1):
                print("no path")
                break
            last_cost = result2[1]
            maze.move(path)
            # maze2.vis_map(path2)
        while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:
            result = search.astar(maze2.get_map(), maze2.start, maze2.end, decode_mode=0, priority=1)

            path2 = result[0]
            if path2[-1] == (-1, -1):
                print("no path")
                break

            maze2.vis_map(path2)
            maze2.move(path2)