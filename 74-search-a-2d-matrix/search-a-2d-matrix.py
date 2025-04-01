class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        def search_in_the_row(row_to_search):
            low = 0
            high = col - 1

            while low <= high:
                mid = (low + high) // 2

                if matrix[row_to_search][mid] == target:
                    return True
                elif matrix[row_to_search][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return False
            

        low_row = 0
        high_row = row - 1

        while low_row  <= high_row:

            mid = (low_row + high_row) // 2

            if matrix[mid][0]<= target <= matrix[mid][col-1]:
                return search_in_the_row(mid)
            elif matrix[mid][0] > target:
                high_row = mid - 1
            else:
                low_row = mid + 1
        
        return False
        


        



        


