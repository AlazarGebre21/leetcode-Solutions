class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            common_mask = ~(ones & twos)
            ones &= common_mask
            twos &= common_mask
        return ones
