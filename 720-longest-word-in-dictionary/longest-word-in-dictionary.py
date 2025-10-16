class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        root = [None for _ in range(27)]
        root[26] = True

        def add(word:str)->None:
            cur = root
            
            for c in word:
                if cur[ord(c)-97] == None:
                    cur[ord(c)-97] = [None for _ in range(27)]
                cur = cur[ord(c)-97]
            
            cur[26] = True
        
        def search(word:str)->bool:
            cur = root

            for c in word:
                if cur[ord(c) - 97] != None and cur[26] == True:
                    cur = cur[ord(c)-97]
                else:
                    return False
            
            return True 

        for word in words:
            add(word)
        
        longest = []

        for word in words:
            if search(word):
                longest.append(word)
                
        longest.sort(key=lambda x:(-len(x),x))

        return longest[0] if len(longest) >= 1 else ""



            
        

