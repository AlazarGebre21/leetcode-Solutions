class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dq = deque([0,1,0])

        for i in range(rowIndex):
            temp = deque()
            for i in range(len(dq) - 1):
                val = dq[i] + dq[i+1]
                temp.append(val)
            dq = temp
            dq.appendleft(0)
            dq.append(0)
        dq.pop()
        dq.popleft()
        return list(dq)