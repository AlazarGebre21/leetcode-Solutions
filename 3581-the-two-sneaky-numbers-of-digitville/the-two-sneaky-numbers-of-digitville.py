class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        has_map = [0] * len(nums)
        result = []
        for i in range(len(nums)):
            has_map[nums[i]] += 1
            if has_map[nums[i]] == 2:
                result.append(nums[i])
        return result
