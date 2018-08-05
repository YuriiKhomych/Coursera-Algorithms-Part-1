

# O(N**2) - Avoid
class QuickFindEager:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        for pos, val in enumerate(self.array):
            if self.array[pos] == self.array[first_node]:
                self.array[pos] = self.array[second_node]

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.array[first_node] == self.array[second_node]
