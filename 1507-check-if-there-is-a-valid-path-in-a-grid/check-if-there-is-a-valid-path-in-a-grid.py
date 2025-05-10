class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
         
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        directions = {
            (0, 1):  ([1, 4, 6], [1, 3, 5]),  # Right
            (0, -1): ([1, 3, 5], [1, 4, 6]),  # Left
            (1, 0):  ([2, 3, 4], [2, 5, 6]),  # Down
            (-1, 0): ([2, 5, 6], [2, 3, 4])   # Up
        }
        
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            x, y = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            for (dx, dy), (curr_types, next_types) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[x][y] in curr_types and grid[nx][ny] in next_types:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        return False
