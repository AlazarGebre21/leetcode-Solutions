class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_map = [0] * len(nums)
        result = []
        for i in range(len(nums)):
            hash_map[nums[i]] += 1
            if hash_map[nums[i]] == 2:
                result.append(nums[i])
        return result
