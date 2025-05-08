class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        class UnionFind:

            def __init__(self, alphabets):
                self.parent = {letter:letter for letter in alphabets}
                self.size = {letter:1 for letter in alphabets}
                self.satisfiability = True
                
            
            def find(self,x):

                if self.parent[x] == x:
                    return x
                
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y,sign):
                if sign == '==':
                    parent_x = self.find(x)
                    parent_y = self.find(y)


                    if self.size[parent_x] >= self.size[parent_y]:
                        self.parent[parent_y] = parent_x
                        self.size[parent_x] += self.size[parent_y]
                    else:
                        self.parent[parent_x] = parent_y
                        self.size[parent_y] += self.size[parent_x]
            

        alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
        # print(alphabets)
        uf = UnionFind(alphabets)
        
        for letter1, eq1, eq2, letter2 in equations:

            sign = eq1 + eq2

            uf.union(letter1, letter2,sign)
        

        for letter1, eq1, eq2, letter2 in equations:

            sign = eq1 + eq2

            if sign == '==':
                if uf.find(letter1) != uf.find(letter2):
                    return False
            else:
                if uf.find(letter1) == uf.find(letter2):
                    return False
                
        
        return True


        
            





        