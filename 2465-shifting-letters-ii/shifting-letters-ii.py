class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        pre_sums = [0] * (len(s) + 1)
        result = []

        # calculating the range sum    
        for start, end, value in shifts:
            if value == 0:
                pre_sums[start] -= 1
                pre_sums[end + 1] += 1
            else:
                pre_sums[start] += 1
                pre_sums[end + 1] -= 1


        # removing the unesseary last element
        pre_sums.pop()

        # calculating the prefix sum
        for i in range(1,len(pre_sums)):
            pre_sums[i] = pre_sums[i] + pre_sums[i-1]
        
        # calculating the shift of each character
        for i in range(len(s)):
            shift = (ord(s[i])+pre_sums[i]) - 97
            result.append(chr((shift % 26) + 97))
        return ''.join(result)



        