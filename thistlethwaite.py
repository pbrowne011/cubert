import sys
import numpy as np
from cubert import cubert
from seedgen import gen_seed
from generate_t1 import generate_phase1_table

# Define the four tables for each phase of the Thistlethwaite algorithm
table_g1 = []
table_g2 = []
table_g3 = []
table_g4 = []

def init_tables():
    # Load tables from files or generate them
    # Initialize tables for each phase
    phase1_table = [-1] * (2**12)
    phase2_table = [-1] * (2**12)
    phase3_table = [-1] * (2**12)
    phase4_table = [-1] * (2**12)

    # Generate tables for each phase
    generate_phase1_table(phase1_table)
    generate_phase2_table(phase2_table)
    generate_phase3_table(phase3_table)
    generate_phase4_table(phase4_table)

    return phase1_table, phase2_table, phase3_table, phase4_table


def is_g1(cube):
    # Check if cube is in G1
    pass

def is_g2(cube):
    # Check if cube is in G2
    pass

def is_g3(cube):
    # Check if cube is in G3
    pass

def is_solved(cube):
    # Check if cube is solved
    pass

def ida_star(cube, max_depth, phase):
    pass

def thistlethwaite(cube):
    init_tables()

    # Solve the cube in four phases
    phase1_solution = ida_star(cube, sys.maxsize, 1)
    phase2_solution = ida_star(cube, sys.maxsize, 2)
    phase3_solution = ida_star(cube, sys.maxsize, 3)
    phase4_solution = ida_star(cube, sys.maxsize, 4)

    # Combine the solutions from each phase
    solution = phase1_solution + phase2_solution + phase3_solution + phase4_solution

    return solution

def main():
    seed = gen_seed()  # You need to import gen_seed from seedgen.py
    scrambled_cube = cubert(seed)
    solution = thistlethwaite(scrambled_cube)

    print(f"Scrambled cube: {seed}")
    print(f"Solution: {solution}")

    scrambled_cube.run_moves(solution)
    print("Is the cube solved? ", is_solved(scrambled_cube))


if __name__ == "__main__":
    main()
