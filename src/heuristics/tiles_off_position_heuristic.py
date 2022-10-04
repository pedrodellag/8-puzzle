from data import matrix_size

def get_num_tiles_off_position(problem_state, solution_state) -> int:
    count = 0

    for i in range(matrix_size):
        for j in range(matrix_size):
            if (problem_state[i][j] != solution_state[i][j]):
                count += 1

    return count
