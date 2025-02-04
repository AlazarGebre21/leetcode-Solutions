class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = {}
        result = []
        for i in range(len(paths)):
            path_array = paths[i].split()
            root = path_array[0]
            for j in range(1,len(path_array)):
                index1 = path_array[j].index('(')
                index2 = path_array[j].index(')')
                key = path_array[j][index1 + 1:index2]
                value = path_array[j][:index1]
                if key in path_dict:
                    path_dict[key].append(root + '/' + value)
                else:
                    path_dict[key] = [root + '/' + value]
        
        for key, value in path_dict.items():
            if len(value) > 1:
                result.append(value)

        return result

            