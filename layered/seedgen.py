import numpy as np
'''
seedgen.py
by Patrick Browne (pbrowne2@bu.edu)
9 February 2023

This script defines a fuction to generate a random starting position
for our magic cube by performing 100 random moves on the cube.

'''

def gen_seed():
    moves = ["w", "o", "g", "r", "y", "b", "w'", "o'", "g'", "r'", "y'", "b'",\
            "w2", "o2", "g2", "r2", "y2", "b2"]
    sequence = ""
    for i in range(100):
        sequence += moves[int(np.random.randint(17))]
    
    return sequence