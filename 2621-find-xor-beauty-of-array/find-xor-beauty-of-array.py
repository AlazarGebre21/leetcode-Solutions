class Solution:
    def xorBeauty(self, nums: List[int]) -> int:


        _xor = 0
        for i in range(len(nums)):
            _xor ^= nums[i]
        return _xor