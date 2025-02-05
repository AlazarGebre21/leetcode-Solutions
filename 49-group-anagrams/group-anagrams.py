class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for string in strs:
            str1 = tuple(sorted(string))
            if str1 in anagram:
                anagram[str1].append(string)
            else:
                anagram[str1] = [string]
        return [values for values in anagram.values()]
            