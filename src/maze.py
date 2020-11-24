import imageio
from node import Node
from stack_frontier import StackFrontier
from queue_frontier import QueueFrontier


class Maze:

    def __init__(self, image):
        """
        :param image: path to source image
        :type image: str
        """
        # Initializing empty fields
        self.explored_nodes = set()
        self.grid = []
        self.solution = None
        self.start, self.target = (None, None)
        self.walls = []
        self.width, self.height = (None, None)

        self.load_image(image)  # Load maze from image file

    def load_image(self, image):
        """
        Load image from file and try to convert it into maze.
        :param image: path to source image
        :type image: str
        """
        print(f"Loading image from {image}")
        self.grid = imageio.imread(image)
        if self.grid is None:
            raise Exception("Couldn't read a file")

        print("Interpreting image")
        self.height, self.width, _ = self.grid.shape
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if all(self.grid[y][x] == [0, 255, 0]):
                    if self.start is not None:
                        raise Exception("More than one starting position found")
                    else:
                        self.start = (x, y)
                        row.append(False)
                        print("Found starting position")
                elif all(self.grid[y][x] == [255, 0, 0]):
                    if self.target is not None:
                        raise Exception("More than one target position found")
                    else:
                        self.target = (x, y)
                        row.append(False)
                        print("Found target position")
                elif all(self.grid[y][x] == [255, 255, 255]):
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

    def get_neighbors(self, state):
        """
        :param state:
        :type state: (int, int)
        """
        x, y = state
        candidates = [
            ("up", (x, y - 1)),
            ("down", (x, y + 1)),
            ("left", (x - 1, y)),
            ("right", (x + 1, y))
        ]

        result = []
        for action, (x, y) in candidates:
            if 0 <= y < self.height and 0 <= x < self.width and not self.walls[y][x]:
                result.append((action, (x, y)))
        return result
    
    def solve(self, mode):
        """
        Solve a maze with algorithm of choice.
        Available algorithms:
          - Depth-first
          - Breadth-first

        :param mode: Algorithm name.
        :type mode: str
        """
        if mode == 'depth-first':
            print("Solving maze with depth-first algorithm")
            frontier = StackFrontier()
        elif mode == 'breadth-first':
            print("Solving maze with breadth-first algorithm")
            frontier = QueueFrontier()
        else:
            raise Exception(f"{mode} mode doesn't exist (yet)!")

        start = Node(self.start, None, None)
        frontier.add(start)

        while True:
            if frontier.is_empty():
                raise Exception("There is no solution for this maze.")

            node = frontier.remove()
            if node.state == self.target:
                print('Solution found!\nRetracing path...')
                cells = []
                actions = []

                while node.parent is not None:
                    cells.append(node.state)
                    actions.append(node.action)
                    node = node.parent

                cells.reverse()
                actions.reverse()
                self.solution = (cells, actions)
                return

            self.explored_nodes.add(node.state)
            for action, state in self.get_neighbors(node.state):
                if not frontier.contains(state) and state not in self.explored_nodes:
                    child = Node(state, node, action)
                    frontier.add(child)

    def solution_output(self, out_path):
        if self.solution is None:
            raise Exception("There is no solution to output. Did you run solve() method?")

        print("Creating image")
        path = self.solution[0]
        new_grid = self.grid

        for y in range(self.height):
            for x in range(self.width):
                if path is not None and (x, y) in path:
                    new_grid[y][x] = [255, 0, 0]

        print("Writing to file")
        imageio.imwrite(out_path, new_grid)
