class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ans = [first]


        for code in encoded:

            ans.append(ans[-1] ^ code)
        
        return ans