class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        clear_path = False
        que = deque([(0,0)])
        count = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]

        def isvalid(r,c):
            return 0<= r < n and 0 <= c < n
        
        if grid[0][0] == 1:
            return -1
        
        
        while que:

            for _ in range(len(que)):

                r, c = que.popleft()
                grid[r][c] = 1

                if r == n - 1 and c == n - 1:
                    clear_path = True
                    break

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc


                    if isvalid(nr,nc) and grid[nr][nc] == 0:
                        que.append((nr,nc))
                        grid[nr][nc] = 1
                        
                
                    
            if not clear_path:
                count += 1  
            else:
                break
                

        return count + 1 if clear_path else -1