class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1;
        elif time > n:
            time_left = time
            forward = True
            backward = False
            count = 0
            while time_left > (n-1):
                count += 1
                time_left = time_left - (n - 1)
                if count % 2 != 0:
                    forward = False
                    backward = True
                else:
                    forward = True
                    backward = False
            if forward:
                return 1 + time_left
            elif backward:
                return n - time_left
        elif time == n:
            return n - 1;