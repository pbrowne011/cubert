from cubert import cubert
from seedgen import gen_seed
from solver import solver
import sys
def main():
    #user input
    if(len(sys.argv)>1):
        command=sys.argv[1]
    else:
        command=""
    print("seed: ",command)
    command = gen_seed()
    cube = cubert(command)
    cube.print_cube()
    
    while True:
        solver(cube)
        command = input("Enter your command(s): ")
        if command == "exit":
            exit()
        
        cube.run_moves(command)
        cube.print_cube()

if __name__ == "__main__":
    main()