from cubert import cubert
from cross import cross
from first_layer import first_layer

def solver(cube):
    cross(cube)
    print("cross solved!")
    first_layer(cube)
    print("first layer solved!")