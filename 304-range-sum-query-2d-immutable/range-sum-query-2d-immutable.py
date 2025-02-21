class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        zero = [0] * n
        matrix.append(zero)
        # def display(matrix,row,col):
        #     for i in range(row):
        #         for j in range(col):
        #             print(matrix[i][j],end=' ')
        #         print()
        # print('original matrix')
        # display(matrix,len(matrix),len(matrix[0]))
        # print(matrix)
        
        for i in range(len(matrix)):
            matrix[i].append(0)

        # print('after zero add matrix')
        # display(matrix,len(matrix),len(matrix[0]))

        for i in range(m):
            for j in range(n):
                matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

        # print('prefix sum matrix')
        # display(matrix,len(matrix),len(matrix[0]))
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.matrix[row2][col2] - self.matrix[row1-1][col2]-self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)