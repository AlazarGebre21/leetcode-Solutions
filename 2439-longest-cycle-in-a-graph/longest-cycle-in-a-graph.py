class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        graph = {}
        _max = -1
        visited = set()

        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i] = edges[i]
            else:
                graph[i] = None

        def cycle_length(my_dict):
            indegree = defaultdict(int)
            node_set = set(my_dict.keys())

            for key, value in my_dict.items():
                if value is not None:
                    indegree[value] += 1

            que = deque([key for key in node_set if indegree[key] == 0])

            while que:
                node = que.popleft()
                if graph[node] is not None:
                    child = graph[node]
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        que.append(child)

            count = 0
            for node in node_set:
                if indegree[node] > 0:
                    count += 1

            return count if count > 0 else -1

        def dfs(node, component):
            visited.add(node)
            child = graph[node]

            if child is not None and child not in visited:
                component[node] = child
                dfs(child, component)
            else:
                if child is not None:
                    component[node] = child
            return component  # <<< always return component

        for i in range(len(edges)):
            if i not in visited:
                component = {}
                _max = max(_max, cycle_length(dfs(i, component)))

        return _max
