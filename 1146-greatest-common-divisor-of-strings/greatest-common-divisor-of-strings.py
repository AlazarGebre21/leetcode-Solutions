class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1 = len(str1)
        len_str2 = len(str2)
        
        def substring(word):
            temp = ""
            len_word = len(word)
            for i in range(len_word):
                temp += word[i]
                if temp*(len_word//len(temp)) == word:
                    return temp
                else:
                    continue
            return temp
        

        def stringGcf(a,b):
            while b > 0:
                a, b = b, a% b
            return a
        
        if len_str1 >= len_str2:
            base_word = substring(str2)

            if (base_word)*(len_str1//len(base_word)) == str1:
                a = len_str1//len(base_word)
                b = len_str2//len(base_word)
                c = stringGcf(a,b)
                return c*base_word
            else:
                return ""
        else:
            base_word = substring(str1)

            if (base_word)*(len_str2//len(base_word)) == str2:
                a = len_str2//len(base_word)
                b = len_str1//len(base_word)
                c = stringGcf(a,b)
                return c*base_word
            else:
                return ""
        
        
        
            

