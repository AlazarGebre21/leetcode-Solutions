class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def my_bisect_left(pos_val_to_be_inserted):
            low = -1
            high = len(citations)

            while low + 1 < high:
                mid = (low + high) // 2

                if citations[mid] >= pos_val_to_be_inserted:
                    high = mid
                else:
                    low = mid
            
            return high

        
        def is_it_h_index(h_index):

            h_papers = len(citations) - my_bisect_left(h_index)

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

