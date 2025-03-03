class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        k = i + 2
        sums = 0
        nums.sort(reverse=True)

        while k < len(nums):
            if nums[j] + nums[k] > nums[i]:
                sums = nums[j] + nums[k] + nums[i]
                break
            i += 1
            j += 1
            k += 1
        return sums

