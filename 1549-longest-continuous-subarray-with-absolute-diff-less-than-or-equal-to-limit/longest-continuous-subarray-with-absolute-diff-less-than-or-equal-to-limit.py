class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        max_len = 0

        min_que = deque([])
        max_que = deque([])

        while i < len(nums) and j < len(nums):

            while min_que and min_que[-1] > nums[j]:
                min_que.pop()
            else:
                min_que.append(nums[j])
            

            while max_que and max_que[-1] < nums[j]:
                max_que.pop()
            else:
                max_que.append(nums[j])
            
            while max_que and min_que and max_que[0] - min_que[0] > limit:
                if max_que and max_que[0] == nums[i]:
                    max_que.popleft()
                
                if min_que and min_que[0] == nums[i]:
                    min_que.popleft()
            
                i += 1
                
            max_len = max(max_len, j - i + 1)
                
            
            j += 1
        
        return max_len
            
            
        