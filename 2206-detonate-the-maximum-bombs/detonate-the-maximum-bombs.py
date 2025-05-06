class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(bombs)):
            x1, y1, r = bombs[i]

            for j in range(len(bombs)):
                
                if j != i:
                    x2, y2, nr = bombs[j]

                    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

                    if d <= r:
                        graph[i].append(j)
        
        # print(graph)

        def dfs(bomb):

            

            for neighbour_bomb in graph[bomb]:

                if neighbour_bomb not in visited:
                    visited.add(neighbour_bomb)
                    dfs(neighbour_bomb)
            

        
        max_bombs_detonated = 0
        for i in range(len(bombs)):
            visited = set()
            visited.add(i)
            dfs(i)
            max_bombs_detonated = max(max_bombs_detonated, len(visited))
        
        return max_bombs_detonated
            
            
            
