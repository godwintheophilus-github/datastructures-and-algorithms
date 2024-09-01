class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, current):
        if current is not None:
            self._inorder_traversal(current.left)
            print(current.value)
            self._inorder_traversal(current.right)

# Example usage:
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Common operations:
print("Common operations:")
print("------------------")

print("1. Insert:")
tree.insert(10)
tree.insert(15)

print("\n2. Inorder Traversal:")
tree.inorder_traversal()
# Output: 2 3 4 5 6 7 8 10 15

# Note: The inorder traversal of a binary search tree visits the nodes in ascending order.