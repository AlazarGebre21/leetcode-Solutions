class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left <= right:
            while left <= right and s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            while left <= right and not s[left].isalnum():
                left += 1
            while left <= right and not s[right].isalnum():
                right -= 1
        return True