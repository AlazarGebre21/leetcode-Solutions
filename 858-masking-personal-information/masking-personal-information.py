class Solution:
    def maskPII(self, s: str) -> str:
        final_s = ''
        if '@' in s:
            index = s.index('@')
            for i in range(len(s)):
                final_s += s[i].lower()
            return final_s[0] + '*****' + final_s[index-1:]


        else:
            s = s.replace('(','').replace(')','').replace('-','').replace('+','').replace(' ','')
            
            unused_country_code = 13 - len(s)
            if unused_country_code == 3:
                return '***' + '-' + "***" + '-' + s[len(s)-4:]
            elif unused_country_code == 2:
                return '+*' + '-' + '***' + '-' + "***" + '-' + s[len(s)-4:]
            elif unused_country_code == 1:
                return '+**' + '-' + '***' + '-' + "***" + '-' + s[len(s)-4:]
            elif unused_country_code == 0:
                return '+***' + '-' + '***' + '-' + "***" + '-' + s[len(s)-4:]


