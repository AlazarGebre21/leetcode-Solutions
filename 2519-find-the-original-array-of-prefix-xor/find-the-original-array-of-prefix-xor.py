class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        

        ans = []
        prev = 0


        for i in range(len(pref)):

            ans.append(pref[i] ^ prev)
            prev = pref[i]
        
        return ans