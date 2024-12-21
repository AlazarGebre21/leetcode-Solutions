class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate_counter = {}
        last_watch = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            duplicate_counter[s[right]] = duplicate_counter.get(s[right],0) + 1

            if duplicate_counter[s[right]] > 1:
                while left <= last_watch[s[right]]:
                    duplicate_counter[s[left]] -= 1
                    left += 1
            
            max_length = max(max_length, right - left + 1)

            last_watch[s[right]] = right

        return max_length

