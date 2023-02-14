from cubert import cubert
from cross import cross
from first_layer import first_layer
from second_layer import second_layer

def solver(cube):
    cross(cube)
    print("cross solved!")
    first_layer(cube)
    print("first layer solved!")
    second_layer(cube)
    print("second layer solved!")