class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        all_visted_index = set()
        visted_index = set()
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                all_visted_index.add(tuple((i,j)))
        row = 0
        col = 0
        while all_visted_index != visted_index and tuple((row,col)) not in visted_index:
            while col < len(matrix[0]) and tuple((row,col)) not in visted_index:
                visted_index.add(tuple((row,col)))
                result.append(matrix[row][col])
                col += 1
            row += 1
            col -= 1
            while row < len(matrix) and tuple((row,col)) not in visted_index:
                result.append(matrix[row][col])
                visted_index.add(tuple((row,col)))
                row += 1
            col -= 1
            row -= 1
            while col >= 0 and tuple((row,col)) not in visted_index:
                visted_index.add(tuple((row,col)))
                result.append(matrix[row][col])
                col -= 1
            row -= 1
            col += 1
            while row >= 0 and tuple((row,col)) not in visted_index:
                visted_index.add(tuple((row,col)))
                result.append(matrix[row][col])
                row-= 1
            col += 1
            row += 1

        return result
            
                

                


            