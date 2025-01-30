class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_x2 = str_x[::-1]
        if str_x == str_x2:
            return True
        else:
            return False
        
