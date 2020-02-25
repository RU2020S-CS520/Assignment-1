import numpy as np
import GridWorld
import search

if __name__ == '__main__':
    maze = GridWorld.Maze(10, 10)

    maze.generate_maze()
    maze.visualize()
    last_cost = None
    while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
        result = search.ada_astar(maze.get_map(), maze.end, maze.start, last_cost, 1)
        path = result[0]
        last_cost = result[1]
        if path[-1] == maze.start:
            print("no path")
            break
        last_cost = result[1]
        maze.vis_map(path)
        maze.move(path)

    #build the maze


