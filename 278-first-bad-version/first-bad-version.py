# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                a = mid
                right = mid - 1
        
        return a
            
                