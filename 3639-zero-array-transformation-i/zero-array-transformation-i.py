class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        prefix_sum = [0] * len(nums)

        for start, end in queries:
            prefix_sum[start] += 1
            if end + 1 < len(prefix_sum):
                prefix_sum[end+1] -= 1
        
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
        
        for i in range(len(prefix_sum)):
            if nums[i] > prefix_sum[i]:
                return False

        return True

        print(prefix_sum)