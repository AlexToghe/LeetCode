/*
 Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
 You must do it in place. (cannot create another vector.)
 */

/*
 The logic to this solution is to iterate through the matrix and check if the point is zero. If the point is zero, add the current row and col to their respective sets.
 Then iterate through the matrix again. check to see if the current index of row and column of the point are in the sets. If they are turn the point to 0.
 
 Thats, it!
 */

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set <int> row; // create set for row
        unordered_set <int> col; // create  set for col

        for (int r = 0; r < matrix.size(); r++){
            for (int c = 0; c < matrix[r].size(); c++){
                if (matrix[r][c] == 0){
                    row.insert(r);
                    col.insert(c);
                }
            }
        }
        for (int r = 0; r < matrix.size(); r++){
            for (int c = 0; c < matrix[r].size(); c++){
                if (row.count(r) || col.count(c)){
                    matrix[r][c] = 0;
                }
            }
        }
    }
};
