class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
    
        while i < len(firstList) and j < len(secondList):
            # Find the intersection range
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
        
            # If it's a valid intersection, add to result
            if start <= end:
                result.append([start, end])
        
            # Move the pointer with the smaller end value
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
    
        return result
