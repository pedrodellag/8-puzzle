import copy
from data import matrix_size

def print_path(root_node, matrix_size):

    if root_node is None:
        return

    print_path(root_node.parent, matrix_size)
    print_matrix(root_node.matrix, matrix_size)


def print_matrix(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print("%d " % (matrix[i][j]), end=" ")

        print()
    print()
    return

def print_summary(open_nodes, visited_nodes, initial_state, solution_path):
    print("\n \n")
    print(" ------------------------------ ")
    print("Estado inicial: \n")
    print_matrix(initial_state, matrix_size)
    print("Nodos abertos: %d \n"%open_nodes.size())
    print("Nodos visitados: %d \n"%visited_nodes.size())
    print("Tamanho total do caminho: %d \n"%solution_path.num_level if solution_path is not None else 0)
    print(" ------------------------------ ")
    return

def determine_tile_coord(matrix, tile_num) -> [int]:
    resulting_arr = []
    tiles_found = 0
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if (matrix[i][j] == tile_num):
                resulting_arr = [i, j]
                tiles_found += 1
    
    if(tiles_found != 1): 
        raise Exception("Error finding tile. Please review your matrix or tile number.")
    
    return resulting_arr