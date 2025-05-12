class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        seen = {0: -1}  # state 0 seen at index -1
        state = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                state ^= (1 << vowel_to_bit[ch])
            
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i

        return max_len
