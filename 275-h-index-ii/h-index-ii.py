class Solution:
    def hIndex(self, citations: List[int]) -> int:

        
        def is_it_h_index(h_index):

            count = 0

            h_papers = len(citations) - bisect_left(citations, h_index)

            if h_papers >= h_index:
                return True
            return False

        low = 0
        high = 1000

        while low <= high:

            mid = (low + high) // 2

            if is_it_h_index(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high

