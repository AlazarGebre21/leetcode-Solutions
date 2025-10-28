class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = [False] * 26

        for letter in sentence:
            if not arr[ord(letter) - 97]:
                arr[ord(letter) - 97] = True
        

        for i in range(len(arr)):
            if not arr[i]:
                return False
        
        return True