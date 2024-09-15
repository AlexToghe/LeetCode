""""
Given an m x n integer matrix, matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place. (cannot create another matrix)
"""

class Solution(object):
    def setZeroes(self, matrix):
        # create a set that keeps track of zeros
        row_set = set()
        col_set = set()

        # iterate through matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # if matrix is zero add the row, and col to our sets that correspond to that zero
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)
        # iterate through the matrix again and if the current row or col is in our set, then turn the point to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0

        return matrix
    