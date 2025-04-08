class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        
        stack = [source]
        visited.add(source)
        while stack:
            vertex = stack.pop()

            if vertex == destination:
                return True

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        
        return False
                
                

        
        
        



            

            
