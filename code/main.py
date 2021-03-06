import search, GridWorld
from copy import deepcopy



if __name__ == '__main__':
    maze = GridWorld.Maze(10, 10)

    maze.generate_maze()
    maze2=deepcopy(maze)
    maze.visualize()

    expanded1=0
    expanded2=0
    while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
        result = search.astar(maze.get_map(), maze.start, maze.end, decode_mode=0, priority=1)

        path = result[0]
        print(path)
        if path[-1] == maze.start:
            print("no path")
            break
        last_cost = result[1]
        print("each time")
        print(result[2])
        expanded1+=result[2]

        maze.vis_map(path)
        maze.move(path)

    heuristics = None
    maze2.visualize()
    while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:

        result2 = search.ada_astar(maze2.get_map(), maze2.start, maze2.end, heuristics, decode_mode=0, priority=1)
        path2 = result2[0]
        print(path2)
        if path2[-1] == maze2.start:
            print("no path")
            break
        last_cost = result2[1]

        expanded2 += result2[2]
        maze2.vis_map(path2)
        maze2.move(path2)

    #build the maze