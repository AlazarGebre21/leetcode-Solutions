class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half, right_half):
             left = 0
             right = 0
             merged = []

             while left < len(left_half) and right < len(right_half):

                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                
                else:
                    merged.append(right_half[right])
                    right += 1
            
             
             while left < len(left_half):
                merged.append(left_half[left])
                left += 1

             while right < len(right_half):
                merged.append(right_half[right])
                right += 1
             
             return merged



        def merge_sort(left,right,arr):

            if left == right:
                return [arr[left]]

            mid = (left + right) // 2

            left = merge_sort(left, mid, arr)

            right = merge_sort(mid + 1, right,arr)

            return merge(left,right)
        
        return merge_sort(0,len(nums) - 1,nums)