import numpy as np
import search, GridWorld
import deepcopy
import matplotlib.pyplot as plt



if __name__ == '__main__':
    expanded1_all=[]
    expanded2_all=[]
    for i in range(50):

        maze = GridWorld.Maze(101, 101)

        maze.generate_maze()
        maze2=deepcopy(maze)
        #maze.visualize()

        expanded1=0
        expanded2=0
        while maze.start[0] != maze.end[0] or maze.start[1] != maze.end[1]:
            result = search.astar(maze.get_map(), maze.start, maze.end)

            path = result[0]
            if path[-1] == maze.start:
                print("no path")
                break
            last_cost = result[1]

            expanded1 += result[2]

            #maze.vis_map(path)
            maze.move(path)
        #maze2.visualize()
        while maze2.start[0] != maze2.end[0] or maze2.start[1] != maze2.end[1]:

            result2 = search.astar(maze2.get_map(), maze2.start, maze2.end)
            path2 = result2[0]
            if path2[-1] == maze2.start:
                print("no path")
                break
            last_cost = result2[1]

            expanded2 += result2[2]
            #maze2.vis_map(path2)
            maze2.move(path2)

        expanded1_all.append(expanded1)
        expanded2_all.append(expanded2)
    print(expanded1_all)
    print(expanded2_all)
    plt.figure('expanded cells')
    y1=expanded1_all
    y2=expanded2_all
    x=np.linspace(1,50,50)
    plt.plot(x,y1,color='blue',label='smaller g-value')
    plt.plot(x,y2,color='red',label='larger g-value')
    plt.xlabel('experiments')
    plt.ylabel('the number of expanded cells')
    plt.legend(loc='best')
    plt.savefig('expanded cells')
    plt.show()
