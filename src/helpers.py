import copy

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
    print("Nodos abertos: %d \n", open_nodes.size())
    print("Nodos visitados: %d \n", visited_nodes.size())
    print("Tamanho total do caminho: %d \n", solution_path.num_level if solution_path is not None else 0)
    print(" ------------------------------ ")
    return
