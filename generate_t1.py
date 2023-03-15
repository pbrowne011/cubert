from collections import deque
from cubert import cubert

def generate_phase1_table(phase1_table):
    # Define the moves allowed in phase 1
    phase1_moves = ["w", "w'", "w2", "o", "o'", "o2", "g", "g'", "g2", "r", "r'", "r2", "b", "b'", "b2", "y", "y'", "y2"]
    
    # Helper function to get the index for phase1_table
    def get_phase1_index(cube):
        # The index is determined by the orientation of edges (12 edges, 2 bits per edge)
        index = 0
        for e in range(12):
            index <<= 2
            index |= cube.get_edge_orientation(e)
        return index

    # Initialize the solved cube state
    solved_cube = cubert()
    solved_index = get_phase1_index(solved_cube)
    phase1_table[solved_index] = 0

    # Perform a breadth-first search to populate the table
    queue = deque([(solved_cube, 0)])
    while queue:
        cube, depth = queue.popleft()
        cube_index = get_phase1_index(cube)
        
        # Generate all possible successors from the current cube state
        for move in phase1_moves:
            new_cube = cube.copy()
            new_cube.run_moves(move)
            new_index = get_phase1_index(new_cube)
            
            # If the new state is not in the table, add it with the updated depth
            if phase1_table[new_index] == -1:
                phase1_table[new_index] = depth + 1
                queue.append((new_cube, depth + 1))

# Example usage:
phase1_table = [-1] * (2**12)
generate_phase1_table(phase1_table)
print(phase1_table)
print("done")
