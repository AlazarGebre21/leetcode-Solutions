class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer,suffix,prefix = [[1] * len(nums) for _ in range(3)]

        for i in range(len(nums)-1):
            prefix[i + 1] = nums[i] * prefix[i]
        print(prefix)

        for j in range(len(nums) - 1, 0,-1):
            suffix[j - 1] = nums[j] * suffix[j]
        print(suffix)
        for i in range(len(nums)):
            answer[i] = prefix[i] * suffix[i]
        return answer
       