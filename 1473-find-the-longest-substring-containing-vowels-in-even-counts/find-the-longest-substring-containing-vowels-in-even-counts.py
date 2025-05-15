class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        

        my_dict ={
            'a':1,
            'e':2,
            'i':4,
            'o':8,
            'u':16
        }
        
        
        previous_prefix = {0:-1}
        prefix = 0
        max_len = 0


        for i in range(len(s)):

            if s[i] in my_dict:
                prefix = prefix ^ my_dict[s[i]]
            
            if prefix in previous_prefix:

                max_len = max(max_len, i - previous_prefix[prefix])

            else:
                previous_prefix[prefix] = i
        

        return max_len

    




    