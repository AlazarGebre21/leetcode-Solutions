class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # o(1) space complexity and 0(n) time complexity solution
        duplicate = []
        for num in nums:
            num = abs(num)
            index = num - 1
            if nums[index] < 0:
                duplicate.append(index + 1)
            else:
                nums[index] *= -1
        return duplicate