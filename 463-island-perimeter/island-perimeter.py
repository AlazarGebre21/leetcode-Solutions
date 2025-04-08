class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        def in_bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        def neighbour_1(row,col):
            count = 0
            for i, j in direction:
                new_row = row + i
                new_col = col + j
                if in_bound(new_row,new_col) and grid[new_row][new_col] == 1:
                    count += 1
            
            return count

        perimeter = 0
        for i in range(len(grid)):
            negihbour_1 = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += (4 - neighbour_1(i,j))
        
        return perimeter
                    
