class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        visited = set()

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def inbound(r,c):
            return 0<= r < rows and 0<= c < cols

        que = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    que.append((r,c))
                    visited.add((r,c))
        
        # print(visited)
        # print(que)
        while que:

            for _ in range(len(que)):

                r, c = que.popleft()

                # print((r,c))

                for dr, dc in directions:

                    nr = dr + r
                    nc = dc + c

                    if inbound(nr,nc) and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        que.append((nr,nc))
                        mat[nr][nc] = mat[r][c] + 1
        
        return mat


