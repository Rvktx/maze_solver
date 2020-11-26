import argparse
from maze import Maze

if __name__ == '__main__':
    # Initializing arguments parser
    parser = argparse.ArgumentParser(description='Maze solver')

    # Adding arguments to parser
    parser.add_argument('--algorithm', type=str, required=False, default='breadth-first',
                        choices=['breadth-first', 'depth-first'],
                        help='Algorithm used in solving the maze')
    parser.add_argument('path', type=str,
                        help='Path of a maze image to solve')
    parser.add_argument('--out-path', '-o', type=str, required=False, default='out.png',
                        help='Output path')
    parser.add_argument('--show-explored', type=bool, required=False, default=False,
                        help='shows explored segments in exported image if set to True')

    # Parsing arguments and starting the program
    args = parser.parse_args()
    maze = Maze(args.path)
    maze.solve(args.algorithm)
    maze.solution_output(args.out_path, args.show_explored)
