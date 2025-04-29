class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        
        piles = [-x for x in piles]
        heapify(piles)
        while k:
            deducted_value = heappop(piles)
            deducted_value = deducted_value // 2
            heappush(piles, deducted_value)
            k -= 1
        piles = [-x for x in piles]        

        return sum(piles)

