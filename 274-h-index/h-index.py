class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        
        h_index = len(citations)
        

        for i in range(len(citations) - 1, -1, -1):
            count = 0
            j = len(citations) - 1
            


            while j >= 0 and citations[j] >= h_index:
                count += 1
                j -= 1
            
            if count >= h_index:
                return h_index

            h_index -= 1
        
        return h_index
       




            





