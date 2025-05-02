class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for idx in range(len(parent)):
            graph[parent[idx]].append(idx)
        ans = 0
        def dfs(x):
            nonlocal ans
            fl,sl = 0,0
            for y in graph[x]:
                l = dfs(y)+1
                if s[x]!=s[y]:
                    if l>fl:
                        sl = fl
                        fl = l
                    elif l>sl:
                        sl = l
            ans = max(ans,fl+sl+1)
            return fl
        dfs(0)
        return ans