class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}
        result = []
        max_time = floor(len(nums)/3)
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = hash_map.get(num,0) + 1
        for key,values in hash_map.items():
            if values > max_time:
                result.append(key)
        return result
