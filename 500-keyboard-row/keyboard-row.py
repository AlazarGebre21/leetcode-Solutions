class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def row(x:str)->bool:
            x = set(list(x))
            first_row = set(list("qwertyuiop"))
            second_row =set(list("asdfghjkl"))
            third_row = set(list("zxcvbnm"))
            if x.issubset(first_row) or x.issubset(second_row) or x.issubset(third_row):
                return True
            else:
                return False
        result = []
        
        for i in range(len(words)):
            if row(words[i].lower()):
                result.append(words[i])
        return result
        