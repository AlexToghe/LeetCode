class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        for(int row = 0; row < grid.size(); row++){
            for(int col = 0; col < grid[row].size(); col++){
                if (grid[row][col] == '1'){
                    
                    DFS(grid, row, col);
                    islands ++;
                }
            }
        }
        return islands;
    }
    void DFS(vector<vector<char>>& grid, int row, int col)   {
        if(row < 0 || row >= grid.size() || col < 0 || col  >= grid[row].size() || grid[row][col] == '0' ){
            return;
        }
        grid[row][col] = '0';
        DFS(grid, row + 1, col);
        DFS(grid, row - 1, col);
        DFS(grid, row, col + 1);
        DFS(grid, row, col - 1);

    }
};
