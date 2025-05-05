class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        

        longest_path = 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]



        directions = [(1,0),(0,-1),(0,1),(-1,0)]

        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r,c):

            if memo[r][c] != -1:
                return memo[r][c]

            max_len = 1 

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if inbound(nr,nc) and matrix[nr][nc] > matrix[r][c]:
                    length = 1 + dfs(nr,nc)
                    max_len = max(max_len, length)
            
            memo[r][c] = max_len
            return max_len





    

        for r in range(rows):
            for c in range(cols):
                val = dfs(r,c)
                longest_path = max(longest_path, val)

        return longest_path
    