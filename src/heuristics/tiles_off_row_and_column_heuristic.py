from data import matrix_size

def calculate_out_of_row_and_column(problem_state, solution_state) -> int:
    sum = 0
    transposed_solution_matrix = transpose_matrix(solution_state)
    transposed_problem_matrix = transpose_matrix(problem_state)
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if((1 if solution_state[i][j] in problem_state[i] else -1) == -1):
                sum += 1
            if((1 if transposed_solution_matrix[i][j] in transposed_problem_matrix[i] else -1)  == -1):
                sum += 1
    
    return sum
    
    
def transpose_matrix(matrix) -> [[int]]:
    return [[ matrix[row][col] for col in range(matrix_size) ] for row in range(matrix_size) ]