from data import matrix_size
from helpers import determine_tile_coord

import numpy as np

def calculate_euclidean_distance(problem_state, solution_state) -> int:
    sum = 0
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            tile_coord = determine_tile_coord(problem_state, solution_state[i][j])
            sum += np.linalg.norm(np.array([i, j]) - np.array(tile_coord))
    
    return sum
    