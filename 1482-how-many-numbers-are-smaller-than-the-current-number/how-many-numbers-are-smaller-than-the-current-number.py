class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result = [0] * len(nums)
        orignal = 0
        for i in range(len(nums)):
            if i == 0:
                result[i] = i
            else:
                if temp[i] == temp[i-1]:
                    result[i] = orignal
                else:
                    result[i] = i
                    orignal = i

        my_dict = {}
        for i in range(len(temp)):
            if temp[i] in my_dict:
                continue
            else:
                my_dict[temp[i]] = result[i]
        

        for i in range(len(nums)):
            if nums[i] in my_dict:
                result[i] = my_dict[nums[i]]

        return result



