class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(arr)
        ans = []
        arr.append(0)

        for i in range(n):

            arr[i] = arr[i] ^ arr[i-1]

        for left, right in queries:
            ans.append(arr[right] ^ arr[left - 1])
        
        return ans


            