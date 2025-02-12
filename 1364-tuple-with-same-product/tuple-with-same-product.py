class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_dict = {}
        number_of_tuple = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in my_dict:
                    my_dict[product].append(tuple((nums[i],nums[j])))
                else:
                    my_dict[product] = [tuple((nums[i],nums[j]))]
        for values in my_dict.values():
            if len(values) == 2:
                number_of_tuple += 8
            elif len(values) < 2:
                continue
            elif len(values) == 3:
                number_of_tuple += 3 * 8
            elif len(values) > 3:
                length = len(values)
                val = length * (length - 1)
                val = val / 2
                val = int(val)
                number_of_tuple += val * 8
        return number_of_tuple


