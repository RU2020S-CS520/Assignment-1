import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors


class Cell:
    def __init__(self):
        self.visited = False
        self.blocked = 0


class Maze:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size = num_rows * num_cols
        self.visited_map = np.zeros((num_rows, num_cols))
        self.start = np.random.randint(0, num_rows, 2)
        self.end = np.random.randint(0, num_rows, 2)
        self.map = np.zeros((num_rows, num_cols))

    def generate_maze(self):  # generate the maze environment by dfs
        grid = [[Cell() for j in range(self.num_rows)] for i in range(self.num_rows)]
        visited_cells = list()  # the stack for dfs
        unvisited_cells = set()  # the set to keep unvisited cells, when the stack is empty, choose any one in this  set to be the start point for dfs
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                unvisited_cells.add((i, j))

        row_start, col_start = random.randint(0, self.num_rows), random.randint(0, self.num_cols)
        row_cur, col_cur = row_start, col_start
        visited_cells.append((row_start, col_start))
        grid[row_start][col_start].visited = True
        unvisited_cells.remove((row_start, col_start))
        while unvisited_cells:

            neighbor_indices = self.find_neighbors((row_cur, col_cur))
            neighbor_indices = [nb for nb in neighbor_indices if not grid[nb].visited]
            if neighbor_indices is not None:
                row_next, col_next = random.choice(neighbor_indices)
                pivot = random.randint(0, 100)
                if pivot < 30:
                    grid[row_next][col_next].blocked = 1  # mark block with probability 0.3
                else:
                    visited_cells.append((row_next, col_next))
                grid[row_next][col_next].visited = True
                unvisited_cells.remove((row_next, col_next))
                row_cur, col_cur = row_next, col_next

            elif visited_cells:  # backtrack
                row_cur, col_cur = visited_cells.pop()
            else:  # select any unvisited cell as start and repeat the process when the stack is empty

                row_cur, col_cur = unvisited_cells.pop()
                visited_cells.append((row_cur, col_cur))
                grid[row_cur][col_cur].visited=True
        self.map = self.map + [[grid[i][j].blocked for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.map[self.start] = 0
        self.map[self.end] = 0
        self.visited_map[self.start] = 1
        self.move([self.start])
        self.visited_map[self.end] = 1
        return

    def reset(self):
        self.visited_map = np.zeros((self.num_rows, self.num_cols))
        self.visited_map[self.start] = 1
        self.move([self.start])
        self.visited_map[self.end] = 1

    def move(self, path):
        for next_pos in path:
            cur = next_pos
            if self.map[cur] == 0:
                self.start = cur
                neighbors = self.find_neighbors(cur)
                for nb in neighbors:
                    self.visited_map[nb] = 1
            else:
                break
        return


    def visualize(self, grid):  # visualize the maze
        # create discrete colormap
        data = [[grid[i][j].blocked for j in range(101)] for i in range(101)]
        cmap = colors.ListedColormap(['white', 'black'])
        bounds = [0, 1, 2]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

        # draw gridlines
        #ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
       # ax.set_xticks(np.arange(-.5, 101, 1));
       # ax.set_yticks(np.arange(-.5, 101, 1));

        plt.show()

    def find_neighbors(self, pos):
        row = pos[0]
        col = pos[1]
        neighbors = list()
        if row - 1 >= 0: # up
            neighbors.append((row - 1, col))
        if row + 1 < self.num_rows:  # down
            neighbors.append((row + 1, col))
        if col - 1 >= 0:  # left
            neighbors.append((row, col - 1))
        if col + 1 < self.num_cols:  # right
            neighbors.append((row, col + 1))
        if len(neighbors) > 0:
            return neighbors
        else:
            return None



