class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que = deque()
        minute_counter = 0
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(r,c):
            return 0<= r < rows and 0<= c < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    que.append((r,c))
        

        while que:

            for _ in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if inbound(nr,nc) and grid[nr][nc] == 1:
                        que.append((nr,nc))
                        grid[nr][nc] = 2
                        count = 1

            minute_counter += count
            count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        
        return minute_counter

            
        
                













                

