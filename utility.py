from queue import PriorityQueue as pq

if __name__ == '__main__':
    ppq = pq()
    ppq.put((3, 5), 5)
    print(ppq.get()[1]);