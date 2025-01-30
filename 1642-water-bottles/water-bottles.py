class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        empty = numBottles
        while numExchange <= empty:
            remainder_bottles = empty % numExchange
            drinked += empty // numExchange
            empty = remainder_bottles + (empty // numExchange)
        return drinked