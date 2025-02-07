class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        number_of_pairs = 0
        left_overs = 0
        my_counter = {}
        for i in range(len(nums)):
            if nums[i] in my_counter:
                my_counter[nums[i]] += 1
            else:
                my_counter[nums[i]] = my_counter.get(nums[i],0) + 1
        for key, values in my_counter.items():
            number_of_pairs += values // 2
            left_overs += values % 2
        return [number_of_pairs,left_overs]