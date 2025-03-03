class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        array = [0] * len(nums)
        result = 0
        for start, end in requests:
            array[start] += 1
            if end + 1 < len(nums):
                array[end + 1] -= 1
        

        for i in range(1,len(array)):
            array[i] = array[i] + array[i-1]

        array.sort()
        nums.sort()
        
        for i in range(len(nums)):
            result += array[i] * nums[i]
        
        return result % (10**9 + 7)