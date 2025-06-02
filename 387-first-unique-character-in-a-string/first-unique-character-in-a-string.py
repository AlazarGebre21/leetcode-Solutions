class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = Counter(s)
        

        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i
        return -1