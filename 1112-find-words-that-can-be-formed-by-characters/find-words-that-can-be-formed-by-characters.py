class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length_sum = 0
        sum_it = True
        for i in range(len(words)):
            my_dict1 = Counter(chars)
            strings = Counter(words[i])
            my_dict1.subtract(strings)

            for values in my_dict1.values():
                if values < 0:
                    sum_it = False
                    break
            if sum_it:
                length_sum += len(words[i])
            sum_it = True
        return length_sum
            
            