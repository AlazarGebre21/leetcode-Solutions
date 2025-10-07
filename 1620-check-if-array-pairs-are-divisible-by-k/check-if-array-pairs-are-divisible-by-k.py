class Solution:
        def canArrange(self, arr: List[int], k: int) -> bool:
            bucket = [0] * k

            for num in arr:
                bucket[num%k] += 1
            

            if k % 2 == 0 and bucket[k//2] % 2 !=  0:
                return False
            
            for i in range(k//2 + 1):
                if bucket[i] != bucket[(-i)%k]:
                    return False
            return True
        