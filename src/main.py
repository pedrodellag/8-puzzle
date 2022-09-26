import copy
import sys
from functools import total_ordering

solution_array = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution_state = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 0]]
    
initial_state = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 0, 8]]

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


def get_num_tiles_off_position(problem_state, solution_state) -> int:
    count = 0
    matrix_size = 3

    for i in range(matrix_size):
        for j in range(matrix_size):
            if(problem_state[i][j] != solution_state[i][j]):
                count += 1

    return count

def create_nodes(matrix, empty_tile_coord, new_empty_tile_coord, num_level, parent) -> Node:
    new_matrix = copy.deepcopy(matrix)

        # Copying data from the parent matrixes to the present matrixes  
    new_mats = copy.deepcopy(matrix)  
  
    # Moving the tile by 1 position  
    x1 = empty_tile_coord[0]  
    y1 = empty_tile_coord[1]  
    x2 = new_empty_tile_coord[0]  
    y2 = new_empty_tile_coord[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]

    costs = get_num_tiles_off_position(new_mats, solution_state)  
  
    new_nodes = Node(parent, new_matrix, new_empty_tile_coord, costs, num_level)  
    return new_nodes 



def print_path(root_path):
    
    if root_path is None:
        return
    
    print_path(root_path.root)


def print_matrix(matrix):
    return


def solve_puzzle(initial, empty_tile_coord):
    return


if __name__ == '__main__':
    nodos_abertos = []
    nodos_visitados = []

    