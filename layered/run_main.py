from cubert import cubert
from seedgen import gen_seed
from solver import solver
import sys
import time
def main():
    #user input
    # startTime = time.time()
    if(len(sys.argv)>1):
        command=sys.argv[1]
    else:
        command=""
    # print("seed: ",command)
    command = gen_seed()
    cube = cubert(command)
    # cube.print_cube()
    
    while True:
        solver(cube)
        break
        # executionTime = (time.time() - startTime)
        # print("Execution time in seconds: " + str(executionTime))
        # print("Number of cubes per second: " + str(int(1 / executionTime)))
        # command = input("Enter your command(s): ")
        # if command == "exit":
        #     exit()
        
        # cube.run_moves(command)
        # cube.print_cube()

if __name__ == "__main__":
    n = 10
    startTime = time.perf_counter()
    for i in range(n):
        main()
    executionTime = time.perf_counter() - startTime
    avgExecutionTime = executionTime / n
    avgCubes = 1 / avgExecutionTime
    print("Total execution time: " + str(executionTime))
    print("Average execution time: " + str(avgExecutionTime))
    print("Average cubes per second: " + str(avgCubes))
