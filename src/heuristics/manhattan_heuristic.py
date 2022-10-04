
from data import matrix_size

solution_array = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def calculate_manhattan_heuristic(problem_state) -> int:
    sum = 0
    problem_arr = transform_into_array(problem_state)
    
    for i in range(len(solution_array)):
        sum += abs(solution_array.index(i) - problem_arr.index(i))

    return sum


def transform_into_array(matrix) -> [int]:
    resulting_arr = []
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            resulting_arr.append(matrix[i][j])
    
    return resulting_arr
