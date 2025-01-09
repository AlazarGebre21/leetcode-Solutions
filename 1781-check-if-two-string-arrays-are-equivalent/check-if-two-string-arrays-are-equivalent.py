class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:            # Concatenate strings in both arrays
        concatenated_word1 = ''.join(word1)
        concatenated_word2 = ''.join(word2)
    
    # Compare the concatenated strings
        return concatenated_word1 == concatenated_word2