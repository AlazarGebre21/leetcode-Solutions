class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        reverse_graph = defaultdict(list)
        n = len(graph)
        outdegree = [0] * n
        

        for i in range(n):  
            for u in graph[i]:
                reverse_graph[u].append(i)
                outdegree[i] += 1
        
        que = deque([i for i in range(n) if outdegree[i] == 0])
        safe_node = [False] * n

        while que:

            terminal_node = que.popleft()
            safe_node[terminal_node] = True

            for neighbour in reverse_graph[terminal_node]:
                outdegree[neighbour] -= 1

                if outdegree[neighbour] == 0:
                    que.append(neighbour)
        

        return [i for i in range(n) if safe_node[i]]

        
                     





        