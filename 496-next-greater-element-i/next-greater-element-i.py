class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        my_dict = {}
        stack = []
        ans = [-1] * len(nums1)

        for i in range(len(nums2)):

            nums2[i] = (nums2[i],i)

        
        for i in range(len(nums2)):
            
            if stack:

                while stack and nums2[i][0] > stack[-1][0]:
                    my_dict[stack[-1][0]] = nums2[i][0]
                    stack.pop()
                else:
                    stack.append(nums2[i])

            else:

                stack.append(nums2[i])

        for i in range(len(nums1)):
            if nums1[i] in my_dict:
                ans[i] = my_dict[nums1[i]]
            else:
                continue

        return ans

        
                    
                    
                    
                    
                
            