class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        max_heap = []
        min_heap = []
        count_continous = 0

        i = 0

        for j in range(len(nums)):

            heappush(max_heap, (-nums[j],j))
            heappush(min_heap, (nums[j],j))

            while abs(-max_heap[0][0] - min_heap[0][0]) > 2:
                i += 1  

                
                while max_heap and max_heap[0][1] < i:
                    heappop(max_heap)
                while min_heap and min_heap[0][1] < i:
                    heappop(min_heap)
                
            
            
            print()
            
            count_continous += (j - i) + 1
            print(i, j)
            
        
        return count_continous