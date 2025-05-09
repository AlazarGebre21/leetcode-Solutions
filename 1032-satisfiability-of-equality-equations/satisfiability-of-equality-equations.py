class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        class UnionFind:

            def __init__(self, alphabets):
                self.parent = {letter:letter for letter in alphabets}
                self.size = {letter:1 for letter in alphabets}
                
            
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
        


        alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        uf = UnionFind(alphabets)

        for letter1, op1, op2, letter2 in equations:

            op = op1 + op2
            uf.union(letter1,letter2,op)
        

        for letter1, op1, op2, letter2 in equations:
            
            op = op1 + op2

            cont1 = uf.find(letter1)
            cont2 = uf.find(letter2)

            if op == '==' and cont1 != cont2:
                return False
            elif op == '!=' and cont1 == cont2:
                return False
        
        return True
                


        
            



