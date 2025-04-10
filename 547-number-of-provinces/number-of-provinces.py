class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count_provinces = 0
        rows = len(isConnected)
        cols = len(isConnected[0])
        graph = defaultdict(set)
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1:
                    graph[r].add(c)
                    graph[c].add(r)

        print(graph)
        
        def dfs(vertex):

           
            visited.add(vertex)

            for n in graph[vertex]:
                if n not in visited:
                    dfs(n)

            return 1
        

        for k in graph:
            if k not in visited:
                count_provinces += dfs(k)
        
        return count_provinces

            
