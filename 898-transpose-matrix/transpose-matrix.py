class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        result = [[0]*row_len for _ in range(col_len)]
        for row in range(row_len):
            for col in range(col_len):
                result[col][row] = matrix[row][col]
        return result