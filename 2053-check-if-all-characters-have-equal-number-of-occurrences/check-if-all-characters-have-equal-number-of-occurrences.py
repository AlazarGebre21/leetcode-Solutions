class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = {}
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = hash_map.get(letter,0) + 1
        good_string_occurance = hash_map[s[0]]

        for values in hash_map.values():
            if values == good_string_occurance:
                continue
            else:
                return False
        return True
