from enum import Enum  

from data import matrix_size
from heuristics.manhattan_heuristic import calculate_manhattan_heuristic
from heuristics.tiles_off_position_heuristic import get_num_tiles_off_position
from heuristics.tiles_off_row_and_column_heuristic import calculate_out_of_row_and_column
from heuristics.euclidean_distance_heuristic import calculate_euclidean_distance

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
    return calculate_euclidean_distance(problem_state, solution_state)

def is_goal(problem_node, solution_state, heuristicsType) -> bool:
    if(heuristicsType == HeuristicsType.NONE):
        return get_num_tiles_off_position(problem_node.matrix, solution_state) == 0
    else: return problem_node.cost == 0