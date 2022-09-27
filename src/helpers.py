def print_path(root_node, matrix_size):
    
    if root_node is None:
        return
    
    print_path(root_node.parent, matrix_size)
    print_matrix(root_node.matrix, matrix_size)


def print_matrix(matrix, matrix_size):
    for i in range(matrix_size):  
        for j in range(matrix_size):  
            print("%d " % (matrix[i][j]), end = " ")  
              
        print()  
    print()
    return