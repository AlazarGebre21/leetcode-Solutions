class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        result = []

        for i in range(len(s)):
            my_dict[s[i]] = i

        i = 0
        j = 0
        while j < len(s):
            partition_index = my_dict[s[j]]
            while i < len(s) and i <= partition_index:
                if my_dict[s[i]] <= partition_index and i < partition_index:
                    i += 1
                elif my_dict[s[i]] > partition_index and i < partition_index:
                    partition_index = my_dict[s[i]]
                    i += 1
                elif my_dict[s[i]] == partition_index and i == partition_index:
                    i += 1
                    result.append(i - j)
                    j = i
                    break
        return result
            

            
        
        