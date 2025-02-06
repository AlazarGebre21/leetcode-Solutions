class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffeld_string = ['o'] * len(s)

        print(shuffeld_string)
        for i in range(len(indices)):
            shuffeld_string[indices[i]] = s[i]
        return ''.join(shuffeld_string)