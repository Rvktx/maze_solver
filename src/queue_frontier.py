from frontier import Frontier


class QueueFrontier(Frontier):
    """ This frontier will be used in breadth-first method. """

    def remove(self):
        if self.is_empty():
            raise Exception("Frontier is empty!")

        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
