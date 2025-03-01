class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        current_sum = 0
        count = 0
        dic = {0:1}
        for num in nums:
            current_sum += num
            previous_sum = current_sum - goal
            if previous_sum in dic:
                count += dic[previous_sum]
            dic[current_sum] = dic.get(current_sum,0) + 1
        
        return count
