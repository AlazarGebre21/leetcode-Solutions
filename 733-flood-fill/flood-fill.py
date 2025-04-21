class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        orignal_color = image[sr][sc]
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()

        def isvalid(r,c):
            return 0<= r < rows and 0<= c < cols and image[r][c] == orignal_color
        
        que = deque([(sr,sc)])
        visited.add((sr,sc))

        while que:
            for _ in range(len(que)):
        
                r,c = que.popleft()
                image[r][c] = color

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if isvalid(nr,nc) and (nr,nc) not in visited:
                        image[nr][nc] = color
                        visited.add((nr,nc))
                        que.append((nr,nc))
        
        return image

        