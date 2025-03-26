class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def checker(mid):
            sums = 0
            counts = 1
            i = 0
            
            while i < len(weights):

                sums += weights[i]

                if sums > mid:
                    sums = weights[i]
                    counts += 1

                    if counts > days:
                        return False
                
                i += 1
            
            
            return True

        

        low = max(weights)
        high = sum(weights)

        

        while low <= high:
            
            mid = (low + high) // 2
         
            if checker(mid):
                high = mid - 1

            else:
                low = mid + 1
            
        return low
        

            

                
        


            


                