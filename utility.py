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
    def top(self):
        #return self.queue.queue[0][0][0]
        pass
    def remove(self,s):
        for i in self.queue.queue:
            if s[0]==i[1][0] and s[1]==i[1][1]:
                self.queue.queue.remove(i)
                return
        return False

    def get(self):
        return self.queue.get()[2]
    def in_open(self,s):
        for i in self.queue.queue:
            if s[0]==i[1][0] and s[1]==i[1][1]:
                return True
        return False



    def empty(self):
        return self.queue.empty()
    """
open_list= PriorityQueue()
open_list.put(5,2,(2,3))
open_list.put(4,3,(5,6))
c=open_list.in_open((2,3))
open_list.remove((2,3))
print(open_list.top())

print(open_list.get())

print(c)
"""
