class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def checker(mid):
            hours = 0
            i = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/mid)
                
                if hours > h:
                    return False
            
            return True
                

        low = 1
        high = max(piles)


        while low <= high:

            mid = (low + high) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
            

