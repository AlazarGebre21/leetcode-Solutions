class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i,j in enumerate(nums):
            if j == target:
                result.append(i)
        return result