class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        my_dict = Counter(s)
        my_dict = dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True))
        print(my_dict)
        for key,value in my_dict.items():
            result += (key * value)
        return result
            