from heapq import heappush, heappop
from node import Node

class priorityQueue:

    def __init__(self):
        self.heap = []
        
    def size(self):
        return len(self.heap)

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)
    
    def find_equal_node(self, node_to_be_found, matrix_size):
        if(isinstance(node_to_be_found, Node) is not True):
            raise Exception("type of variable assigned for comparison is not of type Node")
        
        for node in self.heap:
            if (node.has_matrix_equal_to(node_to_be_found, matrix_size)):
                return True
            
            return False

    def get_costs_list(self) -> [int]:
        costs_list = []
        for item in self.heap:
            if(isinstance(item, Node) is True):
                costs_list.append(item.cost)
        return costs_list
    
    
    def empty(self):
        if not self.heap:
            return True
        else:
            return False
