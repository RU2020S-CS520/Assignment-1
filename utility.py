from queue import PriorityQueue as pq

class PriorityQueue:

    def __init__(self, mode = 0):
        self.queue = pq()
        self.mode = mode

    def put(self, h_cost, g_cost, data):
        if self.mode == 0:
            self.queue.put(((h_cost + g_cost, g_cost), data))
        elif self.mode == 1:
            self.queue.put(((h_cost + g_cost, -g_cost), data))
        return

    def get(self):
        return self.queue.get()[1]

    def empty(self):
        return self.queue.empty()

