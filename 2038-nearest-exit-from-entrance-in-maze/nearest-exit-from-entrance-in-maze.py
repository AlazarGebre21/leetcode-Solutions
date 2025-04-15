class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        

        n = len(maze)
        m = len(maze[0])

        def valid(r,c):

            return 0<= r < n and 0 <= c < m and maze[r][c] == '.'
        

        def end(r,c):
            return r == 0 or c == 0 or r == n - 1 or c == m - 1
        

        queue = deque([tuple(entrance)])
        direction = [(1,0),(0,1),(0,-1),(-1,0)]
        shortest_path = 1
        while queue:

            for _ in range(len(queue)):

                i, j = queue.popleft()
                if maze[i][j] == '+':
                    continue
                maze[i][j] = '+'

                
                for dx, dy in direction:

                    nx = i + dx
                    ny = j + dy
                    
                    if valid(nx,ny):
                        if end(nx,ny):
                            print(nx, ny)
                            return shortest_path

                        queue.append((nx,ny))

            shortest_path += 1
        
        return -1
            

        
