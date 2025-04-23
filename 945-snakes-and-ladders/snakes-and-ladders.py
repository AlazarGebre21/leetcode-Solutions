class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        my_dict = {}
        n = len(board)
        visited = set()
        steps = 0

        r = n - 1
        c = 0
        i = 1
        left_to_right = True

        while r > 0 or c > 0:
            while c < n and left_to_right:
                my_dict[i] = (r,c)
                i += 1
                c += 1
            left_to_right = not left_to_right
            r -= 1
            c -= 1

            while c >= 0 and not left_to_right:
                my_dict[i] = (r,c)
                i += 1
                c -= 1
            left_to_right = not left_to_right
            c += 1
            r -= 1

        if n % 2 == 1:
            r = 0
            c = 0
            while c < n:
                my_dict[i] = (r,c)
                c += 1
                i += 1
        

        print(my_dict)


        que = deque([1])
        visited.add(1)

        while que:
            for _ in range(len(que)):
                sqr = que.popleft()

                if sqr == n ** 2:
                    return steps

                
                for next_square in range(sqr + 1, min(sqr + 6, n ** 2)+1):
                    r, c = my_dict[next_square]
                    dest = board[r][c] if board[r][c] != -1 else next_square

                    if dest not in visited:
                        visited.add(dest)
                        que.append(dest)
        
            steps += 1
        
        return -1