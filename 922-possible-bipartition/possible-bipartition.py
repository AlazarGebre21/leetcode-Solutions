class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        color = [0] * (n + 1)
        visited = set()

        for _from, _to in dislikes:
            graph[_from].append(_to)
            graph[_to].append(_from)
        
        
        
        def can_be_bipartite(vertex):


            for n in graph[vertex]:
                visited.add(vertex)
                if color[n] == color[vertex]:
                    return False
                else:
                    color[n] = 'blue' if color[vertex] == 'red' else 'red'
                    if n not in visited:
                        if not can_be_bipartite(n):
                            return False
            

            return True
        

       
            
        
       
        for i in range(1,n+1):
            if color[i] == 0:
                color[i] = 'red'
                if not can_be_bipartite(i):
                    return False

        return True
        


