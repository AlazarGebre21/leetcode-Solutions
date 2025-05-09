class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
                
        class UnionFind:

            def __init__(self, alphabets):
                self.parent = {letter:letter for letter in alphabets}
                
            
            def find(self,x):

                if self.parent[x] == x:
                    return x
                
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                parent_x = self.find(x)
                parent_y = self.find(y)

                if parent_x != parent_y:

                    if ord(parent_x) <= ord(parent_y):
                        self.parent[parent_y] = parent_x
                    else:
                        self.parent[parent_x] = parent_y
                    
            
        alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        uf = UnionFind(alphabets)
        answer = ''

        for i in range(len(s1)):
            uf.union(s1[i],s2[i])
        

        for i in range(len(baseStr)):
            answer+= uf.find(baseStr[i])
        
        return answer


