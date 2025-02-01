from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        freq = Counter(changed)
        original = []
        
        for num in changed:
            if freq[num] == 0:
                continue  # Skip if already used in a pair
            
            if freq[num * 2] == 0:
                return []  # No valid pair exists
            
            original.append(num)
            freq[num] -= 1
            freq[num * 2] -= 1  # Remove its double from count
        
        return original
