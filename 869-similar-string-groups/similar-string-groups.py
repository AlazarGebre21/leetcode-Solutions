class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def is_similar(a, b):
            diff = []
            for x, y in zip(a, b):
                if x != y:
                    diff.append((x, y))
                if len(diff) > 2:
                    return False
            return len(diff) == 2 and diff[0] == diff[1][::-1] or len(diff) == 0

        class UnionFind:
            def __init__(self, strs):
                self.parent = {s: s for s in strs}
                self.size = {s: 1 for s in strs}

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)
                if px != py:
                    if self.size[px] < self.size[py]:
                        px, py = py, px
                    self.parent[py] = px
                    self.size[px] += self.size[py]

        uf = UnionFind(strs)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    uf.union(strs[i], strs[j])

        return len({uf.find(x) for x in strs})
