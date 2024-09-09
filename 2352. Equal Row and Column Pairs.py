class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        for r in range(n):
            row = grid[r]
            for c in range(n):
                # Build the column as a list
                col = [grid[i][c] for i in range(n)]
                
                # Compare row and column
                if row == col:
                    count += 1
        
        return count
