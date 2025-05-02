class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
        self.ans = []
    
    def find(self, x):

        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            self.ans = [x,y]
            

        if self.size[parent_y] > self.size[parent_x]:

            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x]
        
        else:

            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]
        
         
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges) + 1
        uf = UnionFind(n)

        for i in range(n-1):
            uf.union(edges[i][0], edges[i][1])
        
        return uf.ans
