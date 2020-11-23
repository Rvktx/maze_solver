class Frontier:
    """ Base class for all frontiers. """

    def __init__(self):
        self.frontier = []

    def add(self, node):
        """
        :param node: node to add to the frontier
        :type node: src.node.Node
        """
        self.frontier.append(node)

    def contains(self, state):
        """
        :param state: state to search for
        """
        return any(node.state == state for node in self.frontier)

    def is_empty(self):
        """
        :rtype: bool
        """
        return len(self.frontier) == 0

    def remove(self):
        raise NotImplementedError("This method should be overriden")
