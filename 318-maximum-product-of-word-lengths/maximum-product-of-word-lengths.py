class Solution:
    def maxProduct(self, words: List[str]) -> int:


        def is_equal(arr1, arr2,my_dict):
            xor_sum = 0
            normal_sum = 0

            for char1 in arr1:
                xor_sum = xor_sum ^ my_dict[char1]
                normal_sum = normal_sum + my_dict[char1]
            
            for char2 in arr2:
                xor_sum = xor_sum ^ my_dict[char2]
                normal_sum = normal_sum + my_dict[char2]

            return xor_sum == normal_sum

        
        max_len = 0
        my_dict = {chr(char): 1 << char - ord('a')  for char in range(ord('a'), ord('z') + 1)}

        # print(my_dict)
        arr = [0] * len(words)

        for i in range(len(words)):
            arr[i] = list(set(words[i]))

        # print(arr)

        for i in range(len(arr)):
            first_len = len(words[i])
            for j in range(i + 1, len(arr)):
                second_len = len(words[j])

                if is_equal(arr[i],arr[j],my_dict):
                    max_len = max(max_len, first_len * second_len)
        

        return max_len



