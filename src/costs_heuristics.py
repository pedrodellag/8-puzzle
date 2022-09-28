solution_array = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def calculate_costs(problem_state, solution_state) -> int:
    tiles_off_position_costs = get_num_tiles_off_position(
        problem_state, solution_state)

    return tiles_off_position_costs


def get_num_tiles_off_position(problem_state, solution_state) -> int:
    count = 0

    for i in range(matrix_size):
        for j in range(matrix_size):
            if (problem_state[i][j] != solution_state[i][j]):
                count += 1

    return count
