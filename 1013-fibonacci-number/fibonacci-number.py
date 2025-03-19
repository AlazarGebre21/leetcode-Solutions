class Solution:
    def fib(self, n: int) -> int:
        my_dict = {}
        def rec(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            
            one = my_dict[n-1] if n-1 in my_dict else rec(n-1) 

            two = my_dict[n-2] if n-2 in my_dict else rec(n-2)

            result = one + two

            my_dict[n] = result
            

            return result
        
        return rec(n)


        

