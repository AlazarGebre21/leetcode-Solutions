class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0

        # when there is only 1 element
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n == n
            else:
                return 0 == n

                
        # Handling the case when there is only two element because it is an edge case
        elif len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                return 1 == n
            else:
                return 0 == n
        

        # Finally when there is more than 2 element
        else:
            for i in range(len(flowerbed)):
                if i == 0 and flowerbed[i] == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        planted += 1
                elif i == len(flowerbed) - 1 and flowerbed[i] == 0:

                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        planted += 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        planted += 1

        return planted >= n        