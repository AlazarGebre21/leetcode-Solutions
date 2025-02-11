class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        while n >= 1:
            arr_max = max(arr)
            index = arr.index(arr_max)
            arr = arr[index::-1] + arr[index + 1:]
            result.append(index+1)
            arr = arr[n-1::-1]
            result.append(n)
            arr.pop()
            n = len(arr)
        return result

            
        
        
