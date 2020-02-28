from queue import PriorityQueue as pq

class PriorityQueue:

    def __init__(self, mode):
        self.queue = pq()
        self.mode = mode

    def put(self, h_cost, g_cost, data):
        if self.mode == 0:
            self.queue.put((h_cost + g_cost, g_cost, data))
        elif self.mode == 1:
            self.queue.put((h_cost + g_cost, -g_cost, data))
        return

    def remove(self, s):
        for i in self.queue.queue:
            if s[0] == i[2][0] and s[1] == i[2][1]:
                self.queue.queue.remove(i)
                return
        return False

    def get(self):
        return self.queue.get()[2]

    def empty(self):
        return self.queue.empty()
