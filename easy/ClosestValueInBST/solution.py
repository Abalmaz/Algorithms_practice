"""
Time complexity: avg = O(log(n)), worst case = O(n)
Space complexity: O(log(n))
"""


def findClosestValueInBst(tree: BST, target: int) -> int:
    closest = tree.value
    while tree:
        if abs(target - closest) > abs(target - int(tree.value)):
            closest = tree.value
        if target == tree.value:
            return tree.value
        elif target < int(tree.value):
            tree = tree.left
        elif target > int(tree.value):
            tree = tree.right
        else:
            break
    return closest



class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def create_node(node):
    return BST(node["value"])

def create_BST(data):
    for node in data:
        if node["left"]:
            create_node(data["id"] == [node["left"]])

data = {
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "13", "left": None, "right": "14", "value": 13},
      {"id": "14", "left": None, "right": None, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": None, "value": 2},
      {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
  }
}

root_node = None
for node in data["tree"]["nodes"]:
    if node["id"] == data["tree"]["root"]:
        root_node = BST(node["value"])
        root_node.left = BST(node["left"])
        root_node.right = BST(node["right"])

closest_value = findClosestValueInBst(root_node, 12)
print(closest_value)




# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def get_root(self):
#         return self.root
#
#     def add(self, val):
#         if not self.root:
#             self.root = BST(val)
#         else:
#             self._add(val, self.root)
#
#     def _add(self, val, node):
#         if val < node.value:
#             if node.left:
#                 self._add(val, node.left)
#             else:
#                 node.left = BST(val)
#         else:
#             if node.right:
#                 self._add(val, node.right)
#             else:
#                 node.right = BST(val)
#
#     def view_tree(self):
#         if self.root:
#             self._view_tree(self.root)
#
#     def _view_tree(self, node):
#         if node:
#             self._view_tree(node.left)
#             print(node.value, end=" ")
#             self._view_tree(node.right)
#
# tree = Tree()
# tree.add(10)
# tree.add(15)
# tree.add(5)
# tree.add(13)
# tree.add(22)
# tree.add(14)
# tree.add(2)
# tree.add(1)