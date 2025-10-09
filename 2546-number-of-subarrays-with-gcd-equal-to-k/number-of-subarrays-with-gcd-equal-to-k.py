class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def findGcd(a,b):
            while b > 0:
                a, b = b, a%b
            return a
        

        i = 0
        j = 0
        count = 0

        while i < len(nums):
            tempGcd = nums[i]

            if nums[i] == k:
                tempGcd = nums[i]
            else:
                j += 1
                if j < len(nums):
                    tempGcd = findGcd(nums[i],nums[j])
            
            if tempGcd == k:
                count += 1

            while j < len(nums):


                j += 1
                if j < len(nums):
                    tempGcd = findGcd(tempGcd, nums[j])
                    if tempGcd  == k:
                        count += 1

            
            i += 1
            j = i
        
        return count


        