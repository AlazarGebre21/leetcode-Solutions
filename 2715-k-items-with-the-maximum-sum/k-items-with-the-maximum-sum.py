class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        

        if k <= numOnes:

            return k
        
        elif k <= numOnes + numZeros:

            return numOnes
        
        else:
            temp = k - (numOnes + numZeros)

            return numOnes - temp

