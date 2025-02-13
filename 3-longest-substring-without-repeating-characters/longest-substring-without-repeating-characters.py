class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        non_duplicate = set()
        longest_sub_str = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in non_duplicate:
                non_duplicate.add(s[i])
                longest_sub_str = max(i - j + 1, longest_sub_str)
            elif s[i] in non_duplicate:
                while s[i] in non_duplicate and j < len(s):
                    non_duplicate.remove(s[j])
                    j += 1
                non_duplicate.add(s[i])
                longest_sub_str = max(i - j + 1, longest_sub_str)
        return longest_sub_str
                