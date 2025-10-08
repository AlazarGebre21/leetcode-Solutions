class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

            
        _set1 = set({2,3,5})
        _set2 = set()


        i = 2

        while i*i <= n:

            while n % i == 0:
                
                n //= i
                _set2.add(i)
            
            i += 1
        
        if n > 1:
            _set2.add(n)

        print(_set2)
        

        if _set2 <= _set1:
            return True
        else:
            return False
        

        


