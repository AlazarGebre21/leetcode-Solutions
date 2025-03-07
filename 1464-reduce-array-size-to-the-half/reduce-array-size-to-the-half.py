class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        my_dict = Counter(arr)
        length = len(arr)

        my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)

        for key, value in my_dict:
            length = length - value
            count += 1
            if length <= len(arr)//2:
                return count
        
        return count


