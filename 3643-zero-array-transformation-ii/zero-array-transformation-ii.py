class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def checker(mid):

            arr = [0] * (len(nums))

            for i in range(mid):

                start, end, val  = queries[i]

                arr[start] += val

                if end + 1 < len(arr):

                    arr[end + 1] -= val
            
            for i in range(1, len(arr)):

                arr[i] = arr[i - 1] + arr[i]
        
            
            for a, b in zip(nums, arr):

                if a > b:
                    return False
           
            return True




        low = 0
        
        high = len(queries) - 1
        
        if not checker(len(queries)):
            return -1

        while low <= high:

            mid = (low + high) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        

        return low


