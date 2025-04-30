class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-x for x in nums]

        heapify(nums)


        

        while k > 0:

            kth_largest = heappop(nums)
            k -= 1
        
        return -kth_largest

            
