class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_perimeter = 4
                    # checking top
                    if r > 0 and grid[r-1][c] == 1:
                        max_perimeter -= 1
                    # checking bottom
                    if r < rows - 1 and grid[r+1][c] == 1:
                        max_perimeter -= 1
                    # checking left
                    if c > 0 and grid[r][c-1] == 1:
                        max_perimeter -= 1
                    # checking right
                    if c < cols - 1 and grid[r][c+1] == 1:
                        max_perimeter -= 1
                    
                    perimeter += max_perimeter
        
        return perimeter



                    
