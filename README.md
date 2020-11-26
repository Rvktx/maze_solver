# maze_solver
Simple maze solver written in Python. It takes an image of the maze, solves it using one of implemented algorithms and saves it as a new image with embedded solution. 

### Prerequisites
I have written this in Python 3.8 so it would be ideal to use this version.
To install dependencies in your environment run:

```bash
$ pip3 install -r requirements.txt
```

## How to run
Before you use this app, you have to have a compatible image file.  
Your image should have one starting position marked with a green pixel (#00FF00), 
and one target position marked with a red pixel (#FF0000). 
Walls of the maze should be black pixels (#000000) 
and the rest of a maze should be white background (#FFFFFF). 
For the best result all of the walls and walkable corridors should be 1px wide.  
  
 
You can run default algorithm with:

```bash
$ cd src
$ python run.py /path/to/maze/image
```


## Usage
    usage: run.py [-h] [--algorithm {breadth-first,depth-first}] [--out-path OUT_PATH] path

    Maze solver
    
    positional arguments:
      path                  Path of a maze image to solve
    
    optional arguments:
      -h, --help            show this help message and exit
      --algorithm {breadth-first,depth-first}
                            Algorithm used in solving the maze
      --out-path OUT_PATH, -o OUT_PATH
                            Output path
                            
## Planned features

* More pathfinding algorithms such as Dijkstra algorithm and A*
* Converting wider corridors into segments to improve compatibility with different images
* Optional marking of explored segments to compare efficiency of different algorithms in your case - **DONE**
* ~~Optional~~ time reporting, again to compare efficiency of different algorithms in your case - **DONE**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details