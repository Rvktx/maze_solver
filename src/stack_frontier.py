from frontier import Frontier


class StackFrontier(Frontier):
    """ This frontier will be used in depth-first method. """

    def remove(self):
        if self.is_empty():
            raise Exception("Frontier is empty!")

        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node
