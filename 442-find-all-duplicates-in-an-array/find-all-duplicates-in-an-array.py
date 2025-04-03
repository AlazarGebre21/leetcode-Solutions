class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicate = set()

        i = 0
        while i < len(nums):
            
            correct_pos = nums[i] - 1
            if i == correct_pos:
                i += 1
            else:
                if nums[correct_pos] != nums[i]:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
                else:
                    duplicate.add(nums[correct_pos])
                    i += 1
        
        return list(duplicate)








        # # o(1) space complexity and 0(n) time complexity solution
        # duplicate = []
        # for num in nums:
        #     num = abs(num)
        #     index = num - 1
        #     if nums[index] < 0:
        #         duplicate.append(index + 1)
        #     else:
        #         nums[index] *= -1
        # return duplicate