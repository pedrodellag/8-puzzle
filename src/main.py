import copy
import sys

from costs_heuristics import calculate_costs
from data import initial_state, initial_state_empty_tile_coord, matrix_size, solution_state
from helpers import print_path, print_summary
from node import Node
from pqueue import priorityQueue


def create_node(matrix, empty_tile_coord, new_empty_tile_coord, num_level, parent) -> Node:
    new_matrix = move_matrix_empty_tile_position(
        matrix, empty_tile_coord, new_empty_tile_coord)

    costs = calculate_costs(new_matrix, solution_state)

    new_node = Node(parent, new_matrix, new_empty_tile_coord, costs, num_level)
    return new_node


def move_matrix_empty_tile_position(matrix, empty_tile_coord, new_empty_tile_coord) -> Node:
    new_matrix  = copy.deepcopy(matrix)

    # Moving the tile by 1 position
    x1 = empty_tile_coord[0]
    y1 = empty_tile_coord[1]
    x2 = new_empty_tile_coord[0]
    y2 = new_empty_tile_coord[1]
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]


def solve_puzzle(initial, empty_tile_coord, solution) -> Node:
    initial_node_costs = calculate_costs(initial, solution)

    root_node = Node(None, initial, empty_tile_coord, initial_node_costs, 0)
    
    open_nodes.push(root_node)

    while not open_nodes.empty():

        first_node_in_line = open_nodes.pop()
        # visitados.push()

        if (first_node_in_line.cost == 0):
            return first_node_in_line

        children = generate_children_nodes(first_node_in_line, matrix_size)

        for child in children:
            # IF IS VALID FOR ADDING INTO QUEUE
            open_nodes.push(child)

    return


def generate_children_nodes(node, matrix_size) -> List[Node]:
    children = []

    for i in range(matrix_size):
        # LÓGICADE CRIAÇÃO DE FILHOS
        new_tile_coord = [0, 0]  # logica de coordenadas do movimento

        child = create_node(node.matrix,
                            node.empty_tile_coord,
                            new_tile_coord,
                            node.num_level + 1,
                            node)
        children.push(child)

    return children


if __name__ == '__main__':
    open_nodes = priorityQueue()
    visited_nodes = priorityQueue() #ordena?

    solution_path = solve_puzzle(
        initial_state, initial_state_empty_tile_coord, solution_state)

    # print path
    print_summary(open_nodes, visited_nodes, initial_state, solution_path)
    print(open_nodes)
    print(visited_nodes)
