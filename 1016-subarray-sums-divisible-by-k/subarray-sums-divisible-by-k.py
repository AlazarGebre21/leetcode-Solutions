class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # creating a dictionary to store the remainder
        d = {0:1}
        ans = sums = 0
        for num in nums:
            sums += num
            mo = sums % k
            ans += d.get(mo,0)
            d[mo] = d.get(mo,0) + 1
        return ans
