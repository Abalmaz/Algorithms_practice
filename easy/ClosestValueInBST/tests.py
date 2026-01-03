import pytest

from easy.ClosestValueInBST.solution import findClosestValueInBst
from easy.ClosestValueInBST.solution import BST

test_data = {
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
  },
  "target": 12
}
def create_node(node):
    return BST(node["value"])

def create_BST(data):
    for node in data:
        if node["left"]:
            create_node(data["id"] == [node["left"]])

for node in test_data["tree"]["nodes"]:
    if node["id"] == test_data["tree"]["root"]:
        root_node = BST(node["value"])
        root_node.left = BST(node["left"])
        root_node.right = BST(node["right"])

@pytest.mark.parametrize("tree, target, expected", test_data)
def test_sorted_squared_array(tree, target, expected):
    actual = findClosestValueInBst(tree, target)
    assert actual == expected
