from cross import cross
from first_layer import first_layer
from second_layer import second_layer
from final_layer import final_layer

def solver(cube):
    cross(cube)
    first_layer(cube)
    second_layer(cube)
    final_layer(cube)