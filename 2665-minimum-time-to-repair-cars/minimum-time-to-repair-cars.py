class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def checker(mid):
            cars_fixed = 0
            
            for i in range(len(ranks)):
                cars_fixed += floor(pow(mid/ranks[i],0.5))

            return cars_fixed >= cars


        low = 1
        high = 10 ** 14

        while low <= high:

            mid = (low + high) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        
