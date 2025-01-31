class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = True
        j =  len(s) - 1
        count = 0
        while True:
            if j >= 0 and s[j] == ' ':
                j-=1
                if j >= 0 and s[j] != ' ':
                    while j >= 0 and s[j] != ' ':
                        count += 1
                        j-=1
                    break
                else:
                    continue

            else:
                while j >= 0 and s[j] != ' ':
                    count += 1
                    j-=1
                break
        return count


                
