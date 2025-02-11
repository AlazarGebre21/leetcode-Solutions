class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #removing all the negatives
        minimum = abs(min(nums))
        for i in range(len(nums)):
            nums[i] += minimum

        #hashing the values to index by creating another array to refer by index latter
        hash_map = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            hash_map[nums[i]] += 1

        #reasigning the value of nums by using the index of the hashmaps
        i = 0
        j = 0
        while i < len(hash_map):
            if hash_map[i] == 0:
                i += 1
                continue
            elif hash_map[i] >= 0:
                while hash_map[i] > 0:
                    nums[j] = i
                    hash_map[i] -= 1
                    j += 1
        #removing the minimun from the nums to make the element as expected
        for i in range(len(nums)):
            nums[i] -= minimum
        return nums

