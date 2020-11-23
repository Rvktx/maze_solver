class Node:
    """ This is a node in a maze. """

    def __init__(self, state, parent, action):
        """
        :param state:
        :type state: (int, int)
        :param parent:
        :type parent: Node
        :param action:
        :type action: str
        """
        self.state = state
        self.parent = parent
        self.action = action
