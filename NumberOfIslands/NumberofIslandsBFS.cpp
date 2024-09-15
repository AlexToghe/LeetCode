#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

/**
 * Algorithm Description:
 * This algorithm counts the number of islands in a 2D grid.
 * An island is defined as a group of '1's (land) connected horizontally or vertically.
 * The algorithm uses Breadth-First Search (BFS) to traverse each island and mark it as visited.
 * A set is used to keep track of visited cells, and BFS is initiated for each unvisited '1' encountered.
 * The number of BFS calls corresponds to the number of islands in the grid.
 */

class Solution {
public:
    // Main function to count the number of islands
    int numIslands(vector<vector<char>>& grid) {
        // Return 0 if the grid is empty
        if (grid.empty()) {
            return 0;
        }

        // Get the dimensions of the grid
        int rows = grid.size();
        int cols = grid[0].size();

        // Set to keep track of visited cells
        set<pair<int, int>> visited;

        // Counter for the number of islands
        int islands = 0;

        // BFS helper function to explore the island starting from (r, c)
        auto BFS = [&](int r, int c) {
            queue<pair<int, int>> q;  // Queue for BFS
            visited.insert({r, c});   // Mark the starting cell as visited
            q.push({r, c});           // Add the starting cell to the queue

            // Directions to move in the grid: up, down, left, right
            vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

            // Perform BFS to explore all connected land cells
            while (!q.empty()) {
                auto [row, col] = q.front();  // Get the front element of the queue
                q.pop();                      // Remove it from the queue

                // Explore all 4 possible directions (up, down, left, right)
                for (auto dir : directions) {
                    int nr = row + dir[0];  // New row after moving in direction
                    int nc = col + dir[1];  // New column after moving in direction

                    // Check if the new position is within bounds, is land ('1'), and not visited
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1' && visited.find({nr, nc}) == visited.end()) {
                        visited.insert({nr, nc});  // Mark the new cell as visited
                        q.push({nr, nc});          // Add the new cell to the queue for further exploration
                    }
                }
            }
        };

        // Iterate over all cells in the grid
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                // If the cell is land ('1') and not visited, it's the start of a new island
                if (grid[r][c] == '1' && visited.find({r, c}) == visited.end()) {
                    BFS(r, c);  // Perform BFS to explore the entire island
                    islands++;  // Increment the island count
                }
            }
        }

        return islands;  // Return the total number of islands found
    }
};

