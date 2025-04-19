class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        answer = []
        

        for u, v in redEdges:
            graph[u].append((v,'red'))
        for u, v in blueEdges:
            graph[u].append((v, 'blue'))
        
        
        # print(graph)

        
        def bfs(goal):
            visited = set((0,None))
            que = deque()
            que.append((0,None))
            distance = 0

            if goal == 0:
                return 0

            while que:
                for _ in range(len(que)):
                    node, last_color = que.popleft()

                    if goal == node:
                        return distance
                
                    for neighbour, color in graph[node]:

                        if color != last_color and (neighbour,color) not in visited:
                            visited.add((neighbour,color))
                            que.append((neighbour,color))
            
                distance += 1
            return -1 
                    
        
    



                            
        
        for i in range(n):
            answer.append(bfs(i))
        
        return answer

    
