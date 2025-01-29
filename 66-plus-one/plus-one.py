class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_digit = []
        digit_str = ''
        for i in range(len(digits)):
            digit_str += str(digits[i])
        digit_int = int(digit_str)
        digit_int += 1
        digit_str = str(digit_int)
        for i in range(len(digit_str)):
            large_digit.append(int(digit_str[i]))
        return large_digit
