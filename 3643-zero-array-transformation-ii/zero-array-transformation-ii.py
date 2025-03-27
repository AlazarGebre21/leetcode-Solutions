class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def checker(mid):

            prefix_sum = [0] * len(nums)

            for i in range(mid):
                start, end, val = queries[i]
                prefix_sum[start] += val

                if end + 1 < len(prefix_sum):
                    prefix_sum[end+1] -= val
            
            for i in range(1,len(prefix_sum)):
                prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
            
            for i in range(len(prefix_sum)):
                if nums[i] > prefix_sum[i]:
                    return False

            return True
        


        low = 0 
        high = len(queries) - 1

        if not checker(high + 1):
            return -1
            

        while low <= high:

            mid = (low + high) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

