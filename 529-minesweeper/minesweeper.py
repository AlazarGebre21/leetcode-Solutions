class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        def bomb_counter(r,c):
            bomb = 0
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if inbound(nr,nc) and board[nr][nc] == 'M':
                    bomb += 1
            
            return bomb
        

        que = deque([])
        que.append(click)

        print(que)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        if bomb_counter(r,c) == 0:
            
            board[r][c] = 'B' # but what if it is a digit?
        
        else:
            board[r][c] = str(bomb_counter(r,c))
            return board
        

        while que:

            for _ in range(len(que)):
                r, c = que.popleft()

                
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if inbound(nr,nc) and board[nr][nc] == 'E':
                        bombs = bomb_counter(nr,nc) 
                        if bombs == 0:
                            board[nr][nc] = 'B'
                            que.append((nr,nc))
                        else:
                            board[nr][nc] = str(bombs)
        
        return board