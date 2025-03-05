class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:
            if maxDoubles == 0:
                count = count + (target - 1)
                return count
            elif target % 2 == 0 and maxDoubles:
                target = target//2
                maxDoubles -= 1
                count += 1
            else:
                target -= 1
                count += 1
            
            

        return count

                

            
