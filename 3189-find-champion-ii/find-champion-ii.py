class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        winner = set(range(n))

        for i in range(len(edges)):
            _from, _to = edges[i]
            graph[_from].append(_to)
            winner.discard(_to)
        
        if len(winner) > 1:
            return -1
        else:
            return list(winner)[0]
        
        

        

        
        

        
        