class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(edges)):
            _from, _to = edges[i]
            graph[_from].append(_to)

        

        def dfs(vertex):

            visited.add(vertex)

            for n in graph[vertex]:
                if n not in visited:
                    dfs(n)
        

        for i in range(n):
            visited = set()
            dfs(i)
            if len(visited) == n:
                return i
        
        return -1
        

        
        