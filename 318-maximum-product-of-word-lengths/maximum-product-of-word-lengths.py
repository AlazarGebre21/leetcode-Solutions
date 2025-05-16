class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        max_len = 0
        my_dict = {chr(char): 1 << char - ord('a')  for char in range(ord('a'), ord('z') + 1)}

        # print(my_dict)
        arr = []
        for word in words:
            _or = 0

            for i in word:
                _or |= my_dict[i]
            
            arr.append(_or)
       
        # print(arr)

        for i in range(len(arr)):
            first_len = len(words[i])
            for j in range(i + 1, len(arr)):
                second_len = len(words[j])

                if arr[i] & arr[j] == 0:
                    max_len = max(max_len, first_len * second_len)

                
        

        return max_len



