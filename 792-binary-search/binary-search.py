class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec(l,r):

            mid = (l + r) // 2

            # base case
            if l > r:
                return -1

            
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                return rec(mid + 1, r)

            else:
                return rec(l,mid - 1)
        
        

        l, r = 0, len(nums) - 1

        return rec(l,r)



            