class Solution:
    def hammingWeight(self, n: int) -> int:
        
        set_bits = 0
        _len = n.bit_length()

        if  n and n - 1 == 0:
            return 1
        

        for i in range(_len):

            if 1 & n:
                set_bits += 1
            n = n >> 1
        
        return set_bits