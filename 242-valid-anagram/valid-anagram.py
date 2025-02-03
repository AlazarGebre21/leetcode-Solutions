class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        length = len(s)
        if len(s) != len(t):
            return False
        for i in range(length):
            my_dict[s[i]] = my_dict.get(s[i],0) + 1
        for i in range(length):
            my_dict[t[i]] = my_dict.get(t[i],0) - 1
        for key in my_dict:
            if my_dict[key] != 0:
                return False
            else:
                continue
              
        return True
        
