class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        my_dict = defaultdict(int)
        ans = []
        orignal = list(s)
        
        for i in range(len(orignal)):
            if orignal[i].isalpha():
                orignal[i] = orignal[i].lower()
                
        # print(orignal)
        k = 0

        for i in range(len(s)):
            if s[i].isalpha():
                my_dict[k] = i
                k += 1
        # print(my_dict)


        for i in range(2**k):
            temp = orignal[:]
            j = i
            pos = 0
            while j:
                if j & 1:
                    temp[my_dict[k-pos-1]] = temp[my_dict[k-pos-1]].upper()
                    # print(temp[my_dict[k-pos-1]])
                pos += 1
                j >>= 1

            # print(temp)
            ans.append(''.join(map(str,temp)))

        return ans
                        
                    
                
                
                
                

            

        