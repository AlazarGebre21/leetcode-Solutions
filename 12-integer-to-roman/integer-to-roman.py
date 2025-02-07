class Solution:
    def intToRoman(self, num: int) -> str:
        my_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'CD':400,'CM':900}
        roman = ''
        while num > 0:
            print(num)
            if num >= 1000:
                num -= 1000
                roman += 'M'
                print(num)
                print()
            elif num >= 900:
                num -= 900
                roman += 'CM'
                print(num)
                print()                
            elif num >= 500:
                num -= 500
                roman += 'D'
                print(num)
                print()
            elif num >= 400:
                num -= 400
                roman += 'CD'
                print(num)
                print()            
            elif num >= 100:
                num -= 100
                roman += 'C'
                print(num)
                print()
            elif num >= 90:
                num -= 90
                roman += 'XC'
                print(num)
                print()
            elif num >= 50:
                num -= 50
                roman += 'L'
                print(num)
                print()
            elif num >= 40:
                num -= 40
                roman += 'XL'
                print(num)
                print()
            elif num >= 10:
                num -= 10
                roman += 'X'
                print(num)
                print()
            elif num == 9:
                num -= 9
                roman += 'IX'
                print(num)
                print()
            elif num == 4:
                num -= 4
                roman += 'IV'
                print(num)
                print()
            elif num >= 5:
                num -= 5
                roman += 'V'
                print(num)
                print()
            elif num >= 1:
                num -= 1
                roman += 'I' 
                print(num)
                print()
        return roman         
            
