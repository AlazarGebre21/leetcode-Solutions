class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        upward = True
        downward = False
        rows = len(mat) - 1
        cols = len(mat[0]) - 1 
        i = 0
        j = 0
        while i <= rows and j <= cols:
            while upward and 0 <= i <= rows and 0 <= j <= cols:
                result.append(mat[i][j])
                i -= 1
                j += 1
            i += 1
            j -= 1
            if upward and j < cols:
                i = i
                j += 1
            elif upward and j == cols:
                i += 1
                j = j
            elif downward and i < rows:
                i += 1
                j = j
            elif downward and i == rows:
                j += 1
                i = i
            upward = False
            downward = True
            while downward and 0 <= i <= rows and 0 <= j <= cols:
                result.append(mat[i][j])
                i += 1
                j -= 1
            i -= 1
            j += 1
            if upward and j < cols:
                i = i
                j += 1
            elif upward and j == cols:
                i += 1
                j = j
            elif downward and i < rows:
                i += 1
                j = j
            elif downward and i == rows:
                j += 1
                i = i
            upward = True
            downward = False
        return result


