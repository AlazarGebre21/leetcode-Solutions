class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        else:    
            isPrime = [True for i in range(n)]
            isPrime[0] = isPrime[1] = False
            count = 0

            i = 2

            while i * i <= n:


                if isPrime[i]:
                    j = i * i
                    while j < n:

                        isPrime[j] = False

                        j+=i
                    
                i += 1
            
            for i in range(n):

                if isPrime[i]:
                    count += 1
            
            return count


