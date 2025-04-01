class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def checker(candy):
            candy_count = 0

            for i in range( len(candies)):

                
                candy_count += (floor(candies[i]/candy))

                if candy_count >= k:
                    return True
                
            return False








        low = 1
        high = 10 ** 7

        while low <= high:

            candy = (low + high) // 2

            if checker(candy):
                low = candy + 1
            else:
                high = candy - 1
        
        return low - 1