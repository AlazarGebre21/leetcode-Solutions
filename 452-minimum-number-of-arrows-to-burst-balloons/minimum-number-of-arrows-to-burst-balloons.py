class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # to count the minimum number of arrows used
        count = 0
        current_end = 0
        points.sort(key=lambda x:x[1])

        # Iterating through the array and doing some logic to count the minimum number of arrows
        current_end = points[0][1]
        for start, end in points:

            if start <= current_end <= end:
                continue
            else:
                current_end = end
                count += 1

        return count + 1    

