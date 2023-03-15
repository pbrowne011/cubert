# cubert - A simple text-based Rubik's Cube Simulator

This repository contains two Rubik's Cube solver programs: a layered solution using the beginner's algorithm, and an implementation of the Thistlethwaite algorithm.

The layered solution can solve ~500-600 cubes per second, with average solve times ranging between 1 and 2 milliseconds. It takes between 300 and 500 moves to solve. The Thistlethwaite algorithm has not been implemented yet, but should result in similar solve times. It will take less than 52 moves to solve (and may take as low as 45, depending on my implementation). It will use the IDA* search algorithm to traverse pregenerated tables of moves for each of the four groups.

$~~$













Below is the README.md from the original repository:

---

Just requires python3. 

To run the simulator, you can run:

```
python3 run_main.py "[seed]"
```
Where seed is an option string of moves to premix the cube. So for example, if you want the cube to start with red-clockwise, blue-counterclockwise, yellow clockwise, you can type

```
python3 run_main.py "rb'y"
```

Then the main function will continue to read strings of move inputs, and print out the resulting cube until you type "exit" or ctrl+C.
```
python .\run_main.py
seed:  
{{wwwwwwwww},
{ooooooooo},
{ggggggggg},
{rrrrrrrrr},
{bbbbbbbbb},
{yyyyyyyyy}}
Enter your command(s): w2g'
{{wwwwwwwor},
{rrroowoow},
{bggbggbgg},
{yooyrryrr},
{gggbbbbbb},
{rooyyyyyy}}
Enter your command(s): r
{{wwgwwgwog},
{rrroowoow},
{bgobgybgy},
{yyyrrorro},
{rggwbbwbb},
{robyybyyg}}
Enter your command(s): r'gww
{{wwwwwwwww},
{ooooooooo},
{ggggggggg},
{rrrrrrrrr},
{bbbbbbbbb},
{yyyyyyyyy}}
Enter your command(s): exit

```

There are 6 rotatable faces, and 3 directions for each face. to rotate a face, you type the character of the corresponding color, followed by an optional single quote `'` for counterclockwise, or a `2` for 180 \deg rotation.

* w = white
* o = orange
* g = green
* r = red
* b = blue
* y = yellow
* x = clockwise
* x' = counterclockwise
* x2 = 180 degree rotation

So, in reality, for each state of the cube, there are 3*6 = 18 possible distinct moves you can make (though x2 is equivalent to xx or x'x').

## python
If you make your solver in python, you can import the cubert library and create the cube object directly, or just interact with it via the terminal if you're using another language.

## C++
If you prefer c++, there is an identical c++ implementation of this simulator in the [C++ folder](./c++/)

## Anything Else
If you Would like to make your solver in any other language, the simulator still works as a command line interface, so you can just pipe different programs together with stdout/stdin redirection, or manually type in the results for validation.

Or, if you want to try porting this simulator to antother language, feel free to make a fork, and we can add it to the main repo once we validate it