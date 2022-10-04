from enum import Enum  

from data import matrix_size

solution_array = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class HeuristicsType(Enum):
    NONE = 0
    SIMPLE = 1
    COMPLEX = 2
    
    
def calculate_costs(problem_state, solution_state, heuristicsType, num_level) -> int:
    if(heuristicsType == HeuristicsType.NONE):
            return calculate_costs_without_heuristics(num_level)
    if(heuristicsType == HeuristicsType.SIMPLE):
            return calculate_costs_simple_heuristics(problem_state, solution_state, num_level)
    if(heuristicsType == HeuristicsType.COMPLEX):
            return calculate_costs_complex_heuristics(problem_state, solution_state, num_level)

    raise Exception("heuristicsType Not valid")

def calculate_costs_without_heuristics(num_level) -> int:
    return num_level

def calculate_costs_simple_heuristics(problem_state, solution_state, num_level) -> int:
    return get_num_tiles_off_position(problem_state, solution_state)

def calculate_costs_complex_heuristics(problem_state, solution_state, num_level) -> int:
    sum = 0
    problem_arr = transform_into_array(problem_state)
    
    for i in range(len(solution_array)):
        sum += abs(solution_array.index(i) - problem_arr.index(i))

    return sum


def get_num_tiles_off_position(problem_state, solution_state) -> int:
    count = 0

    for i in range(matrix_size):
        for j in range(matrix_size):
            if (problem_state[i][j] != solution_state[i][j]):
                count += 1

    return count

def transform_into_array(matrix) -> [int]:
    resulting_arr = []
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            resulting_arr.append(matrix[i][j])
    
    return resulting_arr

def is_goal(problem_node, solution_state, heuristicsType) -> bool:
    if(heuristicsType == HeuristicsType.NONE):
        return get_num_tiles_off_position(problem_node.matrix, solution_state) == 0
    else: return problem_node.cost == 0