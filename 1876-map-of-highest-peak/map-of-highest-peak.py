class Solution:
    def highestPeak(self, arr: List[List[int]]) -> List[List[int]]:

        n, m = len(arr), len(arr[0])
        def valid(i, j): return 0 <= i < n and 0 <= j < m
        

        mark = 1

        queue = deque()
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    queue.append((i, j))
                    arr[i][j] = 'w'
                else:
                    arr[i][j] = False
        

        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:


            for _ in range(len(queue)):

                i, j = queue.popleft()



                for dx, dy in move:
                    nx = i + dx
                    ny = j + dy

                    if valid(nx, ny):
                        if not arr[nx][ny]:
                            arr[nx][ny] = mark
                            queue.append((nx, ny))
            mark += 1
        

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 'w':
                    arr[i][j] = 0
        return arr



                    





                