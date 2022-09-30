from functools import total_ordering

@total_ordering
class Node: 

    def __init__(self, parent, matrix, empty_tile_coord, cost, num_level) -> None:
        self.parent = parent  
        self.matrix = matrix  
        self.empty_tile_coord = empty_tile_coord  
        self.cost = cost 
        self.num_level = num_level
        
    def has_matrix_equal_to(self, node, matrix_size) -> bool:
        matrix_A = self.matrix
        matrix_B = node.matrix
        
        for i in range(matrix_size):
            for j in range(matrix_size):
                if (matrix_A[i][j] != matrix_B[i][j]):
                    return 0
        return 1

    def __lt__(self, nxt):
        self.cost < nxt.cost
        
    def __gt__(self, nxt):
        self.cost > nxt.cost
        
