class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        class UnionFind:

            def __init__(self, n):
                self.parent = {i:i for i in range(n)}
                self.size = {i:1 for i in range(n)}
                self.total_weight = 0
                # print(self.parent)
                # print(self.size)
                
            
            def find(self,x):

                if self.parent[x] == x:
                    return x
                
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,weight,x,y):
                parent_x = self.find(x)
                parent_y = self.find(y)

                if parent_x != parent_y:

                    if self.size[parent_x] >= self.size[parent_y]:
                        self.parent[parent_y] = parent_x
                        self.size[parent_x] += self.size[parent_y]
                    else:
                        self.parent[parent_x] = parent_y
                        self.size[parent_y] += self.size[parent_x]
                    
                    self.total_weight += weight

        
        weighted_edges = []
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1,n):

                x2, y2 = points[j]
                val = abs(x2 - x1) + abs(y2-y1)
                weighted_edges.append((val,i,j))
    
        # print(weighted_edges)

        uf = UnionFind(n)
        weighted_edges.sort()

        for edge in weighted_edges:

            weight, s, e = edge
            uf.union(weight,s,e)
        
        return uf.total_weight




                    

