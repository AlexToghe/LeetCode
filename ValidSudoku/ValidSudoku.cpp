class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board){
        // create 3 array of 9 sets for grid_index, row, columns
        unordered_set<char> row_set[9];
        unordered_set<char> col_set[9];
        unordered_set<char> grid_setx[9];
        
        // iterate through board matrix
        for(int row = 0; row < 9; row++){
            for(int col = 0; col< 9; col++){
                char point = board[row][col]; // point
                
                if (point != "."){
                    
                    int grid_index = (r / 3) * 3 + (col / 3); // calculating grid index
                    
                    // check to see if the number is already present in our current indices of row/col/grid sets
                    if (row_set[row].count(point) || col_set[col].count(point) || grid_set[grid_index].count(point)){
                        return false; // if present return false, there is a duplicate
                    
                    }
                    // if no duplicate, add point to sets
                    row_set[row].insert(point);
                    col_set[col].insert(point);
                    grid_set[grid_index].insert(point);
                }
            }
        }
        // return true once iteration through matrix is complete
        return true;
        
        
    }
};
