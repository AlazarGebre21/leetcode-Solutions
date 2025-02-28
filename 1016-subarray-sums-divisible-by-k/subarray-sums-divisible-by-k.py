class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # creating a dictionary to store the remainder
        my_dict = {0:1}
        count = 0
        sums = 0
        modulo = 0

        # Iterating through the array 
        for num in nums:
            sums += num
            modulo = sums % k
            if modulo in my_dict:
                count += my_dict[modulo]
                my_dict[modulo] += 1
            else:
                my_dict[modulo] = my_dict.get(modulo,0) + 1
        return count
