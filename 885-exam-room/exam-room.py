class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            seat = 0
        else:
            # Try to maximize distance
            max_dist = self.students[0]
            seat = 0

            for i in range(1, len(self.students)):
                prev = self.students[i - 1]
                curr = self.students[i]
                d = (curr - prev) // 2
                if d > max_dist:
                    max_dist = d
                    seat = prev + d

            # Check the distance from the last student to the end
            if self.n - 1 - self.students[-1] > max_dist:
                seat = self.n - 1

        bisect.insort(self.students, seat)
        return seat

    def leave(self, p: int) -> None:
        idx = bisect.bisect_left(self.students, p)
        self.students.pop(idx)
