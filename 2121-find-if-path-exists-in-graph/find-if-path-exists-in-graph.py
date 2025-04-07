class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        def dfs(vertex):

            if vertex == destination:
                return True
            
            visited.add(vertex)
            
            for neighbour in graph[vertex]:

                if neighbour not in visited:
                    is_there_path = dfs(neighbour)

                    if is_there_path:
                        return True
                
            return False
        

        return dfs(source)
        



            

            
