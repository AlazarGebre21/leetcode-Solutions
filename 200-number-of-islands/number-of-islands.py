class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        no_island = 0

        # left, right, bottom, up
        directions = [[0,-1],[0,1],[1,0],[-1,0]]

        # is the cell in bound? let us check it using a function
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        def dfs(r,c):
            

            grid[r][c] = '0'


            for add_r, add_c in directions:
                new_r = r + add_r
                new_c = c + add_c
                if inbound(new_r,new_c) and grid[new_r][new_c] == '1':
                    dfs(new_r,new_c)        
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    print(r,c)
                    dfs(r,c)
                    no_island += 1
        
        return no_island









                     