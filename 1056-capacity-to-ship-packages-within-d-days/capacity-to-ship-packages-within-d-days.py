from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity: int) -> bool:
            ships = 1  
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    ships += 1
                    current_load = 0
                current_load += w

            return ships <= days

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid 
            else:
                low = mid + 1 

        return low
