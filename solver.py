from cross import cross
from first_layer import first_layer
from second_layer import second_layer
from final_layer_face import final_layer_face

def solver(cube):
    cross(cube)
    print("cross solved!")
    first_layer(cube)
    print("first layer solved!")
    second_layer(cube)
    print("second layer solved!")
    final_layer_face(cube)