class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        # a function to find the starting position of the island
        def starting_pos(start_r,start_c):
            for start_r in range(rows):
                for start_c in range(cols):
                    if grid[start_r][start_c] == 1:
                        return start_r, start_c

        # right, left, up, down
        direction = [[0,1],[0,-1],[-1,0],[1,0]]

        # Function to check if the cell is inbound or not
        def inbound(row_pos, col_pos):
            return 0 <= row_pos < rows and 0 <= col_pos < cols
        

        
        def dfs(start_r,start_c):
            nonlocal perimeter
            if grid[start_r][start_c] == 0 or inbound(start_r,start_c) == False:
                return perimeter


            grid[start_r][start_c] = -1

            for add_r, add_c in direction:
                new_r = start_r + add_r
                new_c = start_c + add_c

                if inbound(new_r,new_c) and grid[new_r][new_c] == 1:
                    dfs(new_r,new_c)
                elif not inbound(new_r,new_c):
                    perimeter += 1
                elif grid[new_r][new_c] == 0:
                    perimeter += 1
            
            return perimeter
        r, c = starting_pos(0,0)
        return dfs(r,c)
                
                    
        


