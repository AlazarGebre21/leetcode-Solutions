class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def transpose(mat):
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if i <= j:
                        mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            return mat
        def rotate(mat):
            reversed_matrix = [row[::-1] for row in mat]
            reversed_matrix = transpose(reversed_matrix)
            return reversed_matrix
        rotated_mat = rotate(mat)
        for i in range(4):
            if rotated_mat == target:
                return True
            rotated_mat = rotate(rotated_mat)
        return False
        