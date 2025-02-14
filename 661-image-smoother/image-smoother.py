class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        # function for calculating the valid neighboors and returning the valid neighboors for each element in the image
        def neighboors(a,b,rows,cols):
            neighboor = [[-1,-1],[1,1],[0,1],[0,-1],[-1,0],[-1,1],[1,-1],[1,0]]
            result = []
            x = a
            y = b
            for i in range(len(neighboor)):
                x += neighboor[i][0]
                y += neighboor[i][1]
                if 0 <= x < rows and 0 <= y < cols:
                    result.append([x,y])
                x = a
                y = b
            return result
        

        # function to smoothe my image just averaging the each cell with its neighoobors
        def smoother(key,values):
            sums = img[key[0]][key[1]]
            for value in values:
                sums += img[value[0]][value[1]]
            return (sums//(len(values) + 1))





        # creating a dictionary and storing each elements valid neighboors in a dictionary
        my_dict = {}
        smoothed_img = [[0] * len(img[0]) for _ in range(len(img))]
        rows = len(img)
        cols = len(img[0])

        for i in range(rows):
            for j in range(cols):
                my_dict[tuple((i,j))] = neighboors(i,j,rows,cols)
        
        # iterating through the dictionary and accessing the neighboors and smoothing each cell
        for key, values in my_dict.items():
            smoothed_img[key[0]][key[1]] = smoother(key,values)
        return smoothed_img
