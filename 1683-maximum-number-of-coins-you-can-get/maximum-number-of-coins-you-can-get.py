class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        i = 0
        j = len(piles) - 1
        k = j - 1
        while i < k < j:
            result += piles[k]
            i += 1
            k -= 2
            j -= 2
        return result
