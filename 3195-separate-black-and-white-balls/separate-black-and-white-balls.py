class Solution:
    def minimumSteps(self, s: str) -> int:
        counts = 0
        min_swaps = 0
        for i in range(len(s)):
            if s[i] == '0':
                min_swaps += counts
            elif s[i] == '1':
                counts += 1
        return min_swaps