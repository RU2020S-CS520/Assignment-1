import search, GridWorld

if __name__ == '__main__':
    maze = GridWorld.Maze(5, 5)

    maze.test()

    maze.visualize()

    expanded1=0
    expanded2=0
    while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
        result = search.astar(maze.get_map(), maze.start, maze.end, priority=0)

        path = result[0]
        if path[-1] == maze.start:
            print("no path")
            break
        last_cost = result[1]
        print("each time")
        print(result[2])
        print(result[3])
        expanded1+=result[2]

        maze.vis_map(result[3])
        maze.move(path)


    print(expanded1)
