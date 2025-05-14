class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        

        ans = [0] * max(num2.bit_length(), num1.bit_length())
        n = len(ans)

        print(bin(num1))
        print(bin(num2))



        x = num2.bit_count()
       

        while num1 and x:

            ans[n - (num1.bit_length())] = 1

            num1 = num1 ^ (1 << num1.bit_length() - 1)

            x -= 1
        
        i = len(ans) - 1


        while x > 0:

            if ans[i] == 0:
                ans[i] = 1
                x -= 1
            i -= 1
        
        
        ans = ''.join(map(str, ans))

        ans = int(ans, 2)

        return ans        