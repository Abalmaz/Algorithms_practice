"""
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in zigzag order.
  Zigzag order starts at the top left corner of the two-dimensional array, goes
  down by one element, and proceeds in a zigzag pattern all the way to the
  bottom right corner.
"""

def zigzagTraverse(array: list[list[int]]) -> list[int]:
    """
    Patterns to use are a Matrices and Knowing What to Track
    Time complexity: O(N*M), where N is the number of rows and M is the number of columns
    Space complexity: O(N*M), where N is the number of rows and M is the number of columns

    :param array: list[list[int]]
    :return: list[int]
    """
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    going_down = True

    while not (row < 0 or row > height or col < 0 or col > width):
        result.append(array[row][col])

        if going_down:
            # Case: At the bottom or leftmost edge
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            # Case: At the top or rightmost edge
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result

array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(zigzagTraverse(array))