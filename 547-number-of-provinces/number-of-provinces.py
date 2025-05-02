class UnionFind:
    def __init__(self, n):

        self.parent = {i: i for i in range(n)}
        self.size = [1] * (n)
    
    def find(self,x):

        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        
        parent_x = self.find(x)
        parent_y = self.find(y)

        if self.size[parent_x] > self.size[parent_y]:
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]

        elif self.size[parent_y] > self.size[parent_x]:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x]

        else:
            self.parent[parent_y]  = parent_x
            self.size[parent_x] += self.size[parent_y]
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        uf = UnionFind(n)

        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    uf.union(r, c)
        
        no_provinces = 0

        for key, value in uf.parent.items():
            if key == value:
                no_provinces += 1
        
        return no_provinces

            
                
        
