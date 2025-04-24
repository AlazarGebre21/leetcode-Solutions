class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(start):

            if start == destination:
                return True
            
            visited.add(start)
            
            for child in graph[start]:

                if child not in visited:

                    visited.add(child)

                    if dfs(child):
                        return True
            
            return False
        
        return dfs(source)