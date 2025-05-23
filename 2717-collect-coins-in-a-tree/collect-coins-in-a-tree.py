class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = defaultdict(set)

        # Build the undirected tree
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Step 1: prune leaves with no coins
        degree = [len(graph[i]) for i in range(n)]
        queue = deque(i for i in range(n) if degree[i] == 1 and coins[i] == 0)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                graph[neighbor].remove(node)
                degree[neighbor] -= 1
                if degree[neighbor] == 1 and coins[neighbor] == 0:
                    queue.append(neighbor)
            graph[node].clear()

        # Step 2: prune 2 more layers of leaves
        for _ in range(2):
            queue = deque(i for i in range(n) if len(graph[i]) == 1)
            for node in queue:
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                graph[node].clear()

        # Step 3: count remaining edges (each will be visited twice)
        remaining_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
        return remaining_edges * 2


