"""
Time complexity: avg = O(n**2), worst case = O(n**3)
Space complexity: O(n**2)
"""
def findClosestValueInBst(tree, target):
    pass

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = BST(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = BST(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = BST(val)

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.value, end=" ")
            self._view_tree(node.right)

tree = Tree()
tree.add(10)
tree.add(15)
tree.add(5)
tree.add(13)
tree.add(22)
tree.add(14)
tree.add(2)
tree.add(1)


tree.view_tree()
print()