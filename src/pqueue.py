from heapq import heappush, heappop


class priorityQueue:

    def __init__(self):
        self.heap = []
        
    def size(self):
        return len(self.heap)

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False
