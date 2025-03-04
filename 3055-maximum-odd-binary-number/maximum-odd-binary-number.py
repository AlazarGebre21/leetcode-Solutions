class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result = ''
        my_dict = Counter(s)
        print(my_dict['0'])
        if my_dict['1'] == 1:
            result = ('0' * my_dict['0']) + ('1' * my_dict['1'])

        else:
            my_dict['1'] -= 1
            result = my_dict['1'] * '1' + my_dict['0'] *'0' + '1'
        return result