class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            else:
                continue
        result = []
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        diff = len(nums) - len(result)
        result0 = [0] * diff
        result.extend(result0)
        return result