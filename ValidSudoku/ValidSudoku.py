""""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

board:
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
"""
class Solution(object):
    def isValid(self, board):
        if board is None:  # if input board is empty, return False
            return False

        # creating 9 sets to check against duplicates for rows, col, grid index
        # one array for each, row, col, grid index. Representing 9 rows, 9 columns, 9 3x3 grids.
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_index_set = [set() for _ in range(9)]

        # iterate through matrix
        for row in range(len(board)):
            for col in range(len(board[row])):
                point = board[row][col]

                if point != ".":  # only enter conditional statement if the point is anything other than "."
                    grid_index = (row // 3) * 3 + (col // 3)  # calculating grid index

                    # check to see if our point is in our current index of row/col/gridindex/ sets
                    if (point in row_set[row] or
                        point in col_set[col] or
                        point in grid_index_set[grid_index]):

                    # if the point is in our sets, return False, we have a duplicate.
                        return False
                    # if the point is not in any of our sets, add it to row/col/grid/ sets
                    row_set[row].add(point)
                    col_set[col].add(point)
                    grid_index_set[grid_index].add(point)

        # return True when iteration through input board is completed.
        return True

    # Time Complexity O(1), sudoku boards are 9x9 O(n x n) = O(9*9) = O(81) = O(1)
    # Space Complexity O(1)

