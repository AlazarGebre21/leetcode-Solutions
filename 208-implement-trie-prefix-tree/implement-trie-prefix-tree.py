class Trie:
    def __init__(self):
        self.root = [None for i in range(27)]
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur[ord(c)-97] == None:
                cur[ord(c)-97] = [None for i in range(27)]
            cur = cur[ord(c)-97]
        cur[26] = True



    def search(self, word: str) -> bool:    
       cur = self.root
       for c in word:
        if cur[ord(c)-97] != None:
            cur = cur[ord(c)-97]
        else:
            return False

       return True if cur[26] else False
        
      
         
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if cur[ord(c)-97] != None:
                cur = cur[ord(c)-97]
            else:
                return False
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)