class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(left,right):

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        

        left, right = 0, len(nums) - 1

        mid = binary_search(left, right)

        if mid == -1:
            return [-1,-1]
        
        print(mid)


        i = mid
        j = mid

        count_r = 0
        count_l = 0

        while i < len(nums) and nums[i] == target:
            count_r += 1
            i += 1

        while j >= 0 and nums[j] == nums[mid]:
            count_l += 1
            j -= 1
        
        return[mid - count_l + 1, mid + count_r - 1]
        
        

        


