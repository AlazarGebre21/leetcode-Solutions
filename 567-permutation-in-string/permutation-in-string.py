class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if the length of s2 is less than the length of s1 man it is false already
        if len(s1) > len(s2):
            return False
        # declaring a dict for each strings
        s1_dict = {}
        s2_dict = {}

        # iterating through s1 to store it in s1_dict{}
        i = 0
        while i < len(s1):
            s1_dict[s1[i]] = s1_dict.get(s1[i],0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i],0) + 1
            i += 1
        i = 0
        for j in range(len(s1),len(s2)):
            if s1_dict == s2_dict:
                return True
            else:
    
                s2_dict[s2[i]] -= 1
                if s2_dict[s2[i]] == 0:
                    del s2_dict[s2[i]]
                s2_dict[s2[j]] = s2_dict.get(s2[j],0) + 1
                i += 1

        return s1_dict == s2_dict


                
            
            
            

        