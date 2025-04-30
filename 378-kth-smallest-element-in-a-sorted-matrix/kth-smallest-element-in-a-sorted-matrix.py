class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        
        for i in range(len(matrix)):
            ans.extend(matrix[i])
        
        heapify(ans)


        for _ in range(k - 1):
            a = heappop(ans)
        return ans[0]
            