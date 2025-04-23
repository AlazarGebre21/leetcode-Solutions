class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        result = []

        for eq, value in zip(equations, values):
            start, goal = eq
            graph[start].append((goal, value))
            graph[goal].append((start, 1 / value))
        

        
        for start, goal in queries:

            if goal not in graph or start not in graph:
                result.append(-1)
                continue

            que = deque([start])
            parent = {start:(None,1)}
            found = False
            visited = set()

            while que:
                
                for _ in range(len(que)):
                    
                    var = que.popleft()
                    visited.add(var)
                    

                    for neighbor in graph[var]:
                        s, val = neighbor

                        if s not in visited:
                            que.append(s)
                            parent[s] = (var, val)
                        if s == goal:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
                    

            temp = 1
            i = goal

            if goal in parent:
                while parent[i][0]:
                    temp *= parent[i][1]
                    i = parent[i][0]
                result.append(temp)
            else:
                result.append(-1)

                    
        return result