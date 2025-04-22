class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows = len(maze)
        cols = len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def exit(r,c):
            return (r == rows - 1 or r == 0 or c == 0 or c == cols - 1 ) and [r,c] != entrance
        
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        

        que = deque([entrance])
        r, c = entrance
        maze[r][c] = '+'
        steps = 0

        while que:

            for _ in range(len(que)):

                r, c = que.popleft()

                if exit(r,c):
                    return steps

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if inbound(nr, nc) and maze[nr][nc] == '.':
                        que.append((nr,nc))
                        maze[nr][nc] = '+'

                        
            
            steps += 1
        
        return -1



        
