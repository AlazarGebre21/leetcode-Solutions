class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i in range(length):
            if nums[i] > 0:
                index = i + nums[i]
                if index >= length:
                    while index >= length:
                        index -= length
                    result[i] = nums[index]
                elif index < length:
                    result[i] = nums[index]
            elif nums[i] < 0:
                index = i + nums[i]
                while abs(index) >= length:
                    index += length
                result[i] = nums[index]
            elif nums[i] == 0:
                result[i] = nums[i]
        return result


                