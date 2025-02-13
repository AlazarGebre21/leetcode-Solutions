class Solution:
    def validPalindrome(self, s: str) -> bool:
        # declaring the variables
        i = 0
        j = len(s) - 1
        del_time = 0
        
        #iterating through the array from the right and left to check it is valid palidrom given one deletion chance

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                io = i
                jo = j
                not_get_in = True
                i += 1
                while i <= j:
                    if s[i] == s[j]:
                        i += 1
                        j -= 1
                    else:
                        not_get_in = False
                        jo -= 1
                        while io <= jo:
                            if s[io] == s[jo]:
                                io += 1
                                jo -= 1
                            else:
                                return False
                        return True
                if not_get_in:
                    return True
        return True
            



                
            
