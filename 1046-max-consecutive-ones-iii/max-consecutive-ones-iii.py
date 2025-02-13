class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 1,1,1,0,0,0,1,1,1,1,0
        # i
        right= 0
        left = 0
        count = 0
        max_cons_ones = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                count += 1

            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1


            

            max_cons_ones = max(right - left + 1, max_cons_ones)

        return max_cons_ones
