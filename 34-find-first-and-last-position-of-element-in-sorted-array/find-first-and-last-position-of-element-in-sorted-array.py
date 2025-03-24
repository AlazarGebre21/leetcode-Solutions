class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a, b = -1, -1

        def search_right_occurance(left,right):
            nonlocal a
            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    a = mid
                    left = mid + 1
                
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return a
        


        def search_left_occurance(left,right):
            nonlocal b
            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    b = mid
                    right = mid - 1
                
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return b
        
        
        
        return [search_left_occurance(0, len(nums) - 1), search_right_occurance(0, len(nums) - 1)]


        


