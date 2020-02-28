from queue import PriorityQueue as pq
import heapq
import numpy as np


class PriorityQueue:

    def __init__(self, mode=0):
        self.queue = pq()
        self.mode = mode

    def put(self, h_cost, g_cost, data):
        if self.mode == 0:
            self.queue.put((h_cost + g_cost, g_cost, np.random.rand(1), data))
        elif self.mode == 1:
            self.queue.put((h_cost + g_cost, -g_cost, np.random.rand(1), data))
        return

    def get(self):
        return self.queue.get()[3]



