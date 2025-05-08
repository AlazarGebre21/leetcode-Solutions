class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        class UnionFind:

            def __init__(self, n):
                self.parent = {i:i for i in range(n)}
                self.size = {i:1 for i in range(n)}
                
            
            def find(self,x):

                if self.parent[x] == x:
                    return x
                
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                parent_x = self.find(x)
                parent_y = self.find(y)

                if parent_x != parent_y:

                    if self.size[parent_x] >= self.size[parent_y]:
                        self.parent[parent_y] = parent_x
                        self.size[parent_x] += self.size[parent_y]
                        self.size[parent_y] = 1
                    else:
                        self.parent[parent_x] = parent_y
                        self.size[parent_y] += self.size[parent_x]
                        self.size[parent_x] = 1
                    
        

        uf = UnionFind(len(stones))

            

        for i in range(len(stones)):

            x1, y1 = stones[i]

            for j in range(i + 1, len(stones)):
                x2, y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    uf.union(i,j)
        
        count = 0
        
        for key, value in uf.size.items():

            count += (value - 1)

        print(uf.size)

        return count



        