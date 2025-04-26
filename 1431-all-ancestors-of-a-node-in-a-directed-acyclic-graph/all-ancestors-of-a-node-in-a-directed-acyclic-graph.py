class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        indegree = [0] * n
        reachable = [[False] * n for i in range(n)]
        answer = [[] * n for i in range(n)]
        
        for _from, _to in edges:
            graph[_from].append(_to)
            indegree[_to] += 1
            reachable[_from][_to] = True
        


        que = deque([i for i in range(n) if indegree[i] == 0])

        while que:

            for _ in range(len(que)):

                parent = que.popleft()

                for child in graph[parent]:
                    indegree[child] -= 1

                    for other_parent in range(n):

                        if reachable[other_parent][parent]:

                            reachable[other_parent][child] = True
                    
                    if indegree[child] == 0:
                        que.append(child)
        

        for parent in range(n):
            for child in range(n):
                if reachable[parent][child]:
                    answer[child].append(parent)
        
        return answer

                        
        
                

        