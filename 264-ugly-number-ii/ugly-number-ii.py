class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def mixer(array1: list[int], array2: list[int]) -> list[int]:
            temp = []
            for i in range(len(array1)):
                for j in range(len(array2)):
                    temp.append(array1[i] * array2[j])
            return temp

        # Safe exponent limits (covers all needed ugly numbers)
        max2, max3, max5 = 31, 20, 13
        array2 = [2 ** i for i in range(1, max2 + 1)]
        array3 = [3 ** i for i in range(1, max3 + 1)]
        array5 = [5 ** i for i in range(1, max5 + 1)]

        # Pairs
        pairs23 = mixer(array2, array3)
        pairs25 = mixer(array2, array5)
        pairs35 = mixer(array3, array5)

        # Triples (mix pairs with the missing prime)
        triples235 = mixer(pairs23, array5)
        triples325 = mixer(pairs25, array3)
        triples532 = mixer(pairs35, array2)

        # Combine all + 1, dedup, sort
        all_ugly = [1] + array2 + array3 + array5 + pairs23 + pairs25 + pairs35 + triples235 + triples325 + triples532
        unique_ugly = sorted(set(all_ugly))

        return unique_ugly[n - 1]