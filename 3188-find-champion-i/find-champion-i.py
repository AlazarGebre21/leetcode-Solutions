class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        n = len(grid)
        champion = 0
        curr_max_strength = 0

        for r in range(n):
            for c in range(n):
                if r!=c:
                    if grid[r][c] == 1:
                        graph[r].append(c)
        
        for participant,strength in graph.items():
            if len(strength) > curr_max_strength:
                champion = participant
                curr_max_strength = len(strength)
            
        
        print(graph)
        return champion
