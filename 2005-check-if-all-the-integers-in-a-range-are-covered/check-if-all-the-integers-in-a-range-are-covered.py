class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # changing the 2D list into a set
        length = len(ranges)
        checkFor = []
        for i in range(length):
            checkFor.append(ranges[i][0])
            start = ranges[i][0]+1
            end = ranges[i][1]
            while start <= end:
                checkFor.append(start)
                start += 1

        # changing the list to set
        checkFor = set(checkFor)

        # checking all the elements in the left and right range exist in the set
        while left <= right:
            if left in checkFor:
                left += 1
                continue
            else:
                return False
        return True

