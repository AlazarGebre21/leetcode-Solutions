class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        last_char = goal[len(goal)-1]
        indexes = []
        for i in range(len(s)):
            if last_char == s[i]:
                indexes.append(i)
        for index in indexes:
            after_shift_s = s[index + 1:] + s[:index + 1]
            if after_shift_s == goal:
                return True
        return False