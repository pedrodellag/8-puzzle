from functools import total_ordering

@total_ordering
class Node: 

    def __init__(self, parent, matrix, empty_tile_coord, cost, num_level) -> None:
        self.parent = parent  
        self.matrix = matrix  
        self.empty_tile_coord = empty_tile_coord  
        self.cost = cost 
        self.num_level = num_level

    def __lt__(self, next):
        self.cost < next.cost
