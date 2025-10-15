class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = [None for _ in range(27)]

        def add(word:str)->None:
            cur = root
            
            for c in word:
                if cur[ord(c)-97] == None:
                    cur[ord(c)-97] = [None for _ in range(27)]
                cur = cur[ord(c)-97]
            
            cur[26] = True
        
        def search(word:str)->tuple[str, bool]:
            cur = root
            ans = ''
            for c in word:
                idx = ord(c) - 97
                if cur[idx] is None:
                    return '', False
                cur = cur[idx]  # Move first
                ans += c        # Then add to ans
                if cur[26]:     # Then check current node
                    return ans, True
            return '', False
        

        for word in dictionary:
            add(word)
        
        array = sentence.split()
        ans = []

        for word in array:
            rot, isRoot = search(word)
            if isRoot:
                ans.append(rot)
            else:
                ans.append(word)

        print(ans) 
        return ' '.join(ans)
            



        