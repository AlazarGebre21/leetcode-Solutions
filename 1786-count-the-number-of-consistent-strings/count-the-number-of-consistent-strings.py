class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        fine = True
        for word in words:
            for i in word:
                if i not in allowed:
                    fine = False
            if fine:
                count += 1
            fine = True
        return count
                    