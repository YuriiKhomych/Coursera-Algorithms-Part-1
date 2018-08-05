

# O(N + M lg* N) - wicked fast - use this
class WeightedQuickUnionPathCompression:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]
        self.weight = [num for num in range(nodes)]

    # Follows parent pointers to actual root
    def root(self, parent):
        while parent != self.array[parent]:
            self.array[parent] = self.array[self.array[parent]]
            parent = self.array[parent]
        return parent

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        if self.root(first_node) == self.root(second_node):
            return

        if self.weight[first_node] < self.weight[second_node]:
            self.array[first_node] = self.root(second_node)
            self.weight[second_node] += self.weight[first_node]
        else:
            self.array[second_node] = self.root(first_node)
            self.weight[first_node] += self.weight[second_node]

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)
