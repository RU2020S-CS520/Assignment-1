import numpy as np
import GridWorld
import search

if __name__ == '__main__':
    for i in range(50):
        maze = GridWorld.Maze()
        while maze.start != maze.end:
            result = search.astar(maze.map, maze.start, maze.end)
            path = result[0]
            last_cost = result[1]
            maze.move(path)

            result = search.astar(maze.map, maze.start, maze.end)
            path = result[0]
            last_cost = result[1]
            maze.move(path)
        while maze.start != maze.end:
            result = search.astar(maze.map, maze.start, maze.end, last_cost)
            path = result[0]
            last_cost = result[1]
            maze.move(path)

    #build the maze


