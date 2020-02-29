import numpy as np
import search, GridWorld
from copy import deepcopy
import matplotlib.pyplot as plt



if __name__ == '__main__':
    expanded1_all=[]
    expanded2_all=[]
    for i in range(50):

        maze = GridWorld.Maze(101, 101)

        maze.generate_maze()
        maze2=deepcopy(maze)
        # maze.visualize()

        expanded1=0
        expanded2=0
        flag = True
        while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
            k = 0
            result = search.astar(maze.get_map(), maze.start, maze.end, decode_mode=0, priority=1)

            path = result[0]
            expanded1+=result[2]
            if path[-1] == (-1, -1):
                print("no path")
                break
            # print(path)
            #maze.vis_map(path)
            maze.move(path)
        #maze2.visualize()
        print("#########")
        while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:

            result2 = search.astar(maze2.get_map(), maze2.start, maze2.end, decode_mode=1, priority=1)
            path2 = result2[0]
            expanded2 += result2[2]
            if path2[-1] == (-1, -1):
                print("no path")
                break
            # print(path2)
            # maze2.vis_map(result2[1])
            maze2.move(path2)

        expanded1_all.append(expanded1)
        expanded2_all.append(expanded2)
    print(expanded1_all)
    print(expanded2_all)
    print(np.mean(expanded1_all))
    print(np.mean(expanded2_all))
    print(np.var(expanded1_all))
    print(np.var(expanded2_all))
    plt.figure('expanded cells')
    y1=expanded1_all
    y2=expanded2_all
    x=np.linspace(1,50,50)
    plt.plot(x,y1,color='blue',label='forward')
    plt.plot(x,y2,color='red',label='backward')
    plt.xlabel('experiment number')
    plt.ylabel('the number of expanded cells')
    plt.legend(loc='best')
    plt.savefig('expanded cells')
    plt.show()