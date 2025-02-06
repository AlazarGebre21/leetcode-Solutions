class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        print(players)
        i = 0
        while len(players) > 1:
            i += k - 1
            i = i % len(players)
            players.remove(players[i])
        return players[0]
