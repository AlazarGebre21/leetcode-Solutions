class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        def xor(nums):

            ans = 0
 
            for num in nums:
                ans ^= num
            
            return ans
        

        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            
            return 0
        
        else:

            if len(nums1) % 2 == 0:

                return xor(nums1)
            
            elif len(nums2) % 2 == 0:

                return xor(nums2)
            
            else:
                
                a = xor(nums1)
                b = xor(nums2)

                return a^b
        