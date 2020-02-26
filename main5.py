import numpy as np
import GridWorld
import search
from copy import deepcopy
import matplotlib.pyplot as plt



if __name__ == '__main__':
    expanded1_all=[]
    expanded2_all=[]
    for i in range(2):

        maze = GridWorld.Maze(101, 101)

        maze.generate_maze()
        maze2=deepcopy(maze)
        #maze.visualize()

        expanded1=0
        expanded2=0
        last_cost = None
        while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:
            result2 = search.ada_astar(maze2.get_map(), maze2.start, maze2.end, last_cost, mod=1, decode_mode=0)
            path2 = result2[0]
            last_cost = result2[1]
            if path2[-1] == maze2.start:
                print("no path")
                break
            last_cost = result2[1]
            expanded2 += result2[2]

            maze.move(path2)
        while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
            result = search.astar(maze.get_map(), maze.start, maze.end,mod=1,decode_mode=0)

            path = result[0]
            print(path)
            if path[-1] == maze.start:
                print("no path")
                break
            last_cost = result[1]

            expanded1+=result[2]

          #  maze.vis_map(path)
            maze.move(path)
        #maze2.visualize()


        expanded1_all.append(expanded1)
        expanded2_all.append(expanded2)

    plt.figure('repeated and adaptive')
    y1=expanded1_all
    y2=expanded2_all
    x=np.linspace(1,50,50)
    plt.plot(x,y1,color='blue',label='repeated')
    plt.plot(x,y2,color='red',label='adaptive')
    plt.xlabel('experiments')
    plt.ylabel('the number of expanded cells')
    plt.legend(loc='best')
    plt.savefig('expanded cells')
    plt.show()