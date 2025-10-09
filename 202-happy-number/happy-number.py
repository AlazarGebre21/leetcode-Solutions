class Solution:
    def isHappy(self, n: int) -> bool:
        _set = set()

        while n != 1:
            _sum = 0

            while n != 0:
                _sum += ((n % 10)**2)
                n //= 10
            
            if _sum in _set:
                return False
            
            _set.add(_sum)
            n = _sum
        

        return True


                


            



            