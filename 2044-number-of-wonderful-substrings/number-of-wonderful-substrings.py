class Solution:
    def wonderfulSubstrings(self, word: str) -> int:


        count = defaultdict(int)
        count[0] = 1  # empty prefix
        mask = 0
        res = 0
        
        for ch in word:
            # Flip the bit corresponding to this character
            bit = ord(ch) - ord('a')
            mask ^= (1 << bit)

            # Case 1: All characters appear even times (mask seen before)
            res += count[mask]

            # Case 2: Only one character has odd count (try flipping each bit once)
            for i in range(10):
                res += count[mask ^ (1 << i)]
            
            # Update count of current mask
            count[mask] += 1
        
        return res
