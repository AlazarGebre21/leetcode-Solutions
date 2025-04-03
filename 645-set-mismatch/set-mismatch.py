class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        duplicate_lost = set()
        i = 0

        while i < len(nums):
            correct_pos = nums[i] - 1

            if correct_pos == i:
                i += 1
            else:
                if nums[i] == nums[correct_pos]:
                    duplicate_lost.add(nums[i])
                    i += 1
                    
                else:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
        
        duplicate_lost = list(duplicate_lost)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate_lost.append(i + 1)


        return duplicate_lost