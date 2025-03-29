class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        else:
            l = 0
            r = len(nums) - 1
            minimum = float('inf')
            while l < r:

                mid = (l + r) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
            return nums[l]
