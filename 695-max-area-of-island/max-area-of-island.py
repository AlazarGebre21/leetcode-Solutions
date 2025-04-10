class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        #up down left right
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def inbound(r,c):
            return 0 <= r < rows and 0<= c < cols

        def dfs(r,c):
            
            count = 1
            grid[r][c] = 0

            for a, b in directions:
                new_r = r + a
                new_c = c + b

                if inbound(new_r,new_c) and grid[new_r][new_c] == 1:
                    count += dfs(new_r,new_c)
            
            return count
            



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area
