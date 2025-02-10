class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_valid(board,values,a,b):
            n = len(values)
            for k in range(n):
                i,j = values[k]
                if i == a or j == b:
                    return False
            tr_i, tr_j = a//3, b//3
            for i in range(tr_i*3,tr_i*3+3):
                for j in range(tr_j*3,tr_j*3+3):
                    if board[a][b] == board[i][j] and i != a and j != b:
                        return False
            return True 
            
        my_dict = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in my_dict:
                        valid = check_valid(board,my_dict[board[i][j]],i,j)
                        if valid:
                            my_dict[board[i][j]].append([i,j])
                        else:
                            return False
                    else:
                        my_dict[board[i][j]] = [[i,j]]
        return True

