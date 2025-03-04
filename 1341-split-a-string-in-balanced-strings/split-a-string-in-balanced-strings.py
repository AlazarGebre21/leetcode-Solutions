class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Representing 's' as a mix of 1 for R and -1 for L in the form of an array

        array = [0] * len(s)
        subs = 0
        sums = 0
        
        # Iterating through a for loop to create the integer equivalent for the above stiring
        for i in range(len(s)):
            if s[i] == 'R':
                array[i] += 1
            else:
                array[i] -= 1
        
        # calculating the substring whenever we got a sum of 0
        for i in range(len(array)):
            sums += array[i]
            if sums == 0:
                subs += 1
        
        return subs
            
        

