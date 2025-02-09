class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)  # Count occurrences of each answer
        total_rabbits = 0

        for x, freq in count.items():
            groups = (freq + x) // (x + 1)  # Number of groups needed
            total_rabbits += groups * (x + 1)  # Total rabbits accounted

        return total_rabbits
