class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {}
        prefix_count = []


        def add(word: str) -> None:
            cur = root

            for c in word:
                if c not in cur:
                    cur[c] = {}
                    cur = cur[c]
                    cur[count] = cur.get(count, 0) + 1
                else:
                    cur = cur[c]
                    cur[count] += 1
        
        def count(word: str) -> int:
            cur = root
            total = 0

            for c in word:
                cur = cur[c]
                total += cur[count]
            
            return total
        

        for word in words:
            add(word)
        
        for word in words:
            prefix_count.append(count(word))
        
        return prefix_count


        
    