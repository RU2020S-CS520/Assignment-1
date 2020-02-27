import numpy as np
import GridWorld
import search
from copy import deepcopy
import matplotlib.pyplot as plt
if __name__ == '__main__':
    expanded1_all = []
    expanded2_all = []
    total1 = 0
    total2 = 0
    for i in range(50):
        times1 = 0
        times2 = 0
        maze = GridWorld.Maze(101, 101)
        last_cost = None
        expanded1 = 0
        expanded2 = 0
        maze.generate_maze()
        maze2 = deepcopy(maze)
        while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
            result = search.ada_astar(maze.get_map(), maze.start, maze.end, last_cost, 0, 1)
            path = result[0]
            last_cost = result[1]
            expanded1 += result[2]
            times1 += 1
            if path[-1] == (-1, -1):
                print("no path")
                break

            # print(path)
            # maze.vis_map(path)
            maze.move(path)
            # print(result[2])
            # print(expanded1)
        total1 = total1 + expanded1
        expanded1_all.append(expanded1)
        print("##########")

        while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:
            result2 = search.astar(maze2.get_map(), maze2.start, maze2.end, 0, 1)

            path2 = result2[0]
            last_cost = result2[1]
            times2 += 1
            expanded2 += result2[2]
            if path2[-1] == (-1, -1):
                print("no path")
                break
            # maze2.vis_map(path2)
            maze2.move(path2)
            # print(result2[2])
        total2 = total2 + expanded2
        expanded2_all.append(expanded2)

    print(total1, total2)
    plt.figure('repeated and adaptive')
    y1 = expanded1_all
    y2 = expanded2_all
    x = np.linspace(1, 50, 50)
    plt.plot(x, y1, color='blue', label='adaptive')
    plt.plot(x, y2, color='red', label='repeated')
    plt.xlabel('experiments')
    plt.ylabel('the number of expanded cells')
    plt.legend(loc='best')
    plt.savefig('expanded cells')
    plt.show()

