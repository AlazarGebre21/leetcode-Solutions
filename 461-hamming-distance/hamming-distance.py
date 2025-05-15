class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        n = max(x,y).bit_length()
        hamming_distance = 0

        for i in range(n):
            first = x & 1
            second = y & 1
            
            if first ^ second:

                hamming_distance += 1
            
            x = x >> 1
            y = y >> 1
        
        return hamming_distance
