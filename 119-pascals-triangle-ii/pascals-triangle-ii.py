class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(rowIndex):


            if rowIndex == 0:
                return [1]

            arr = pascal(rowIndex-1)
            temp = []
            for i in range(len(arr)-1):
                temp.append(arr[i] + arr[i+1])
            

            
            return [1] + temp + [1]

        arr = []
        return pascal(rowIndex)