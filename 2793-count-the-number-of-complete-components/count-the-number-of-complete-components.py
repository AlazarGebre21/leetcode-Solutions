class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        graph = defaultdict(list)
        complete_component = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)
        

        def dfs(vertex, component_edge, component_node):

            visited.add(vertex)
            component_node.append(vertex)
            for n in graph[vertex]:
                component_edge.append((max(vertex, n), min(vertex,n)))
                if n not in visited:
                    dfs(n,component_edge,component_node)
        

        for i in range(n):
            if i not in visited:
                component_edge = []
                component_node = []
                

                dfs(i, component_edge, component_node)

                
                v = len(component_node)
                e = len(set(component_edge))

                total_edge = (v * (v - 1)) / 2

                if total_edge == e:
                    
                    complete_component += 1
        

        return complete_component

                
        




        





