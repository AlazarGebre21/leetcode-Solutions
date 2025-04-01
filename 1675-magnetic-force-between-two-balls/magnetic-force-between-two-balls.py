class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def checker(force):
            count_balls = 1
            start = position[0] + force

            for i in range(1,len(position)):
                if position[i] >= start:
                    count_balls += 1
                    start = position[i] + force
                
                if count_balls == m:
                    return True
            
            return False




        low = 1
        high = max(position) - min(position)

        while low <= high:

            force = (low + high) // 2

            if checker(force):
                low = force + 1
            else:
                high = force - 1
        
        return high

       
