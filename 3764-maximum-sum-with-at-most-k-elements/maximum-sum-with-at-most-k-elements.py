class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        arr = []

        for indx,row in enumerate(grid):
            arr.extend(nlargest(limits[indx], row))
        
        arr = nlargest(k, arr)
        return sum(arr)