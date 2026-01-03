from decorators.SpeedTestWrapper import timed
"""
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.
  Spiral order starts in the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.
"""

@timed(10)
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result

@timed(10)
def spiralTraverse_v2(array: list[list[int]]) -> list[int]:
    result = []
    ar = array.copy()
    while ar:
        result += ar.pop(0)
        ar = list(zip(*ar))[::-1]
    return result


array = [[19, 32, 33, 34, 25, 8], [16, 15, 14, 13, 12, 11], [18, 31, 36, 35, 26, 9], [1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [17, 30, 29, 28, 27, 10]]
print(spiralTraverse(array))
print(spiralTraverse_v2(array))
