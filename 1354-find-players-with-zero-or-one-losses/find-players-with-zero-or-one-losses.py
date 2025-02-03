class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        ans_a, ans_b = [], []
        for match in matches:
            winners[match[0]] = winners.get(match[0],0) + 1
            losers[match[1]] = losers.get(match[1],0) + 1

        for key in winners:
            winner_has_not_lost = losers.get(key,0)
            if winner_has_not_lost == 0:
                ans_a.append(key)
        
        for key in losers:
            one_time_loser = losers.get(key)
            if one_time_loser == 1:
                ans_b.append(key)
        return [sorted(ans_a),sorted(ans_b)]


                

            
        
