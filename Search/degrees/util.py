class Node():
    def __init__(self, state, parent, actions):
        self.state = state      # State
        self.parent = parent    # Parent of it state
        self.actions = actions  # The Actions perfomed to get into it state
    
    def __repr__(self):
        return f'({self.state} <- {self.parent}; {self.actions})'

    def __eq__(self, other):
        return isinstance(other, Node) and (self.state == other.state and self.parent == other.parent)

    def __hash__(self):
        return hash((self.state, self.parent))

    def get_state(self):
        return self.state
    
    def get_parent(self):
        return self.parent
    
    def get_actions(self):
        return self.actions


# Stacki
class StackFrontier():

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

# Queue
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
