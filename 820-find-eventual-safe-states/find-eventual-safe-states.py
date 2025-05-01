class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        reverse_graph = defaultdict(list)
        n = len(graph)
        indegree = [0] * n
        

        for parent in range(n):  
            for child in graph[parent]:
                reverse_graph[child].append(parent)
                indegree[parent] += 1

        print(indegree)
         
        que = deque([i for i in range(n) if indegree[i] == 0])
        safest_node = [False] * n

        while que:

            terminal_node = que.popleft()
            safest_node[terminal_node] = True

            for neighbour in reverse_graph[terminal_node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    que.append(neighbour)
        

        return [i for i in range(n) if safest_node[i]]

        
                     





        