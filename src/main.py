import copy
import sys

from costs_heuristics import calculate_costs
from data import initial_state, initial_state_empty_tile_coord, matrix_size, solution_state
from helpers import print_matrix, print_path, print_summary
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

    x1, y1 = empty_tile_coord[0], empty_tile_coord[1]
    x2, y2 = new_empty_tile_coord[0], new_empty_tile_coord[1]

    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    
    return new_matrix


def solve_puzzle(initial, empty_tile_coord, solution) -> Node:
    initial_node_costs = calculate_costs(initial, solution)
    MAX_TRY_COUNT = 2000

    root_node = Node(None, initial, empty_tile_coord, initial_node_costs, 0)
    
    open_nodes.push(root_node)

    while not open_nodes.empty():

        print("\n Open Nodes Queue Size: ", open_nodes.size())
        first_node_in_queue = open_nodes.pop()
        print("\n Visited Nodes Queue Size: ", visited_nodes.size())
        visited_nodes.push(first_node_in_queue)
        
        if(visited_nodes.size() > MAX_TRY_COUNT):
            raise Exception("more than " + MAX_TRY_COUNT + " visited, solution not found")

        #print("\n cost: %d", first_node_in_queue.cost)
        #print_path(first_node_in_queue, matrix_size)
        
        print("\n Node to be Evaluated. Node cost: ", first_node_in_queue.cost)
        
        if (first_node_in_queue.cost == 0):
            return first_node_in_queue

        children = generate_children_nodes(first_node_in_queue, matrix_size)

        for child in children:
            if(open_nodes.find_equal_node(child, matrix_size) is not True and 
               visited_nodes.find_equal_node(child, matrix_size) is not True):
                open_nodes.push(child)

    return

def isSafe(x, y, matrix_size):  
      
    return x >= 0 and x < matrix_size and y >= 0 and y < matrix_size  

def generate_children_nodes(node, matrix_size) -> [Node]:
    children = []
    max_moves = 4
    
    # bottom, left, top, right  
    rows = [ 1, 0, -1, 0 ]  
    cols = [ 0, -1, 0, 1 ]  

    for i in range(max_moves):
        new_tile_coord = [  
            node.empty_tile_coord[0] + rows[i],  
            node.empty_tile_coord[1] + cols[i], ]  
        #print("current tile coord: ", node.empty_tile_coord[0], node.empty_tile_coord[1])
        #print("row: ", rows[i])
        #print("col: ", cols[i])
        #print("new tile coord: ", new_tile_coord[0], new_tile_coord[1])          
        if isSafe(new_tile_coord[0], new_tile_coord[1], matrix_size):  
            child = create_node(node.matrix,
                                node.empty_tile_coord,
                                new_tile_coord,
                                node.num_level + 1,
                                node)
            children.append(child)

    print("\n\n ---------- ")
    print("parent node matrix: ")
    print_matrix(node.matrix, matrix_size)
    
    for child in children:
        print("Child created: \n")
        print_matrix(child.matrix, matrix_size)
    print(" ---------- ")
    return children


if __name__ == '__main__':
    open_nodes = priorityQueue()
    visited_nodes = priorityQueue() #ordena?

    solution_path = solve_puzzle(
        initial_state, initial_state_empty_tile_coord, solution_state)
    
    print_path(solution_path, matrix_size)
    print_summary(open_nodes, visited_nodes, initial_state, solution_path)
