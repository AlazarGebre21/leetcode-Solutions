class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # changing all the elements to string
        nums = list(map(str,nums))

        # Sorting the element from the largest to smallest by using selection sort and some technique
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        # joining the result using the join function from the array
        result = ''.join(nums)
        if result[0] == '0':
            return '0'
        else:
            return result


