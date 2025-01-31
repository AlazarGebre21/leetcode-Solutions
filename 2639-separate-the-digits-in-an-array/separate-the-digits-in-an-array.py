class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answers = []
        str1 = ''
        for i in range(len(nums)):
            str1 += str(nums[i])
        for i in range(len(str1)):
            answers.append(int(str1[i]))
        return answers
