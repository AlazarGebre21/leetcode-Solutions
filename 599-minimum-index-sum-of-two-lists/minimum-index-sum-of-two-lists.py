class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_index_sum = float('inf')
        dict1 = {}
        dict2 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        for j in range(len(list2)):
            dict2[list2[j]] = j
        for key, value in dict1.items():
            if key in dict2:
                current_sum = dict2[key] + value
                if min_index_sum > current_sum:
                    result = []
                    result.append(key)
                    min_index_sum = current_sum
                elif min_index_sum == current_sum:
                    result.append(key)
        return result




