class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in range(n):
            for col in range(n):
                if col < n - col - 1:
                    image[row][col], image[row][n-col-1] = image[row][n-col-1], image[row][col]
        for row in range(n):
            for col in range(n):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
        return image
