import copy
import sys

from costs_heuristics import calculate_costs
from data import initial_state, initial_state_empty_tile_coord, matrix_size, solution_state
from helpers import is_in_list, print_matrix, print_path, print_summary
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

    root_node = Node(None, initial, empty_tile_coord, initial_node_costs, 0)
    
    open_nodes.push(root_node)

    while not open_nodes.empty():

        first_node_in_queue = open_nodes.pop()
        visited_nodes.push(first_node_in_queue)

        #print("\n cost: %d", first_node_in_queue.cost)
        #print_path(first_node_in_queue, matrix_size)
        
        
        if (first_node_in_queue.cost == 0):
            return first_node_in_queue

        children = generate_children_nodes(first_node_in_queue, matrix_size)

        for child in children:
            if(is_in_list(child, open_nodes, matrix_size) or 
               is_in_list(child, visited_nodes, matrix_size)):
                return
            
            open_nodes.push(child)

    return

def isSafe(x, y, matrix_size):  
      
    return x >= 0 and x < matrix_size and y >= 0 and y < matrix_size  

def generate_children_nodes(node, matrix_size) -> list[Node]:
    children = []
    
    # bottom, left, top, right  
    rows = [ 1, 0, -1, 0 ]  
    cols = [ 0, -1, 0, 1 ]  

    for i in range(matrix_size):
        new_tile_coord = [  
            node.empty_tile_coord[0] + rows[i],  
            node.empty_tile_coord[1] + cols[i], ]  
        
        print("new tile coord: %d %d", new_tile_coord[0], new_tile_coord[1])          
        if isSafe(new_tile_coord[0], new_tile_coord[1], matrix_size):  
            child = create_node(node.matrix,
                                node.empty_tile_coord,
                                new_tile_coord,
                                node.num_level + 1,
                                node)
            children.append(child)

    print("\n\n parent node matrix: ")
    print_matrix(node.matrix, matrix_size)
    print("---------- \n ")
    for child in children:
        print("Child created: \n")
        print_matrix(child.matrix, matrix_size)
    
    return children


if __name__ == '__main__':
    open_nodes = priorityQueue()
    visited_nodes = priorityQueue() #ordena?

    solution_path = solve_puzzle(
        initial_state, initial_state_empty_tile_coord, solution_state)
    
    print_path(solution_path, matrix_size)
    print_summary(open_nodes, visited_nodes, initial_state, solution_path)
