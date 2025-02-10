class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(image)):
            flip = image[i][::-1]
            invert = list(map(lambda x: 1 - x, flip))
            result.append(invert)
        return result