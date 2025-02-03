class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict ={}
        result = []
        for path in paths:
            lst = path.split()
            index = 1
            while index < len(lst):
                files, content = lst[index][:-1].split("(")
                abs_path = lst[0]+'/'+files
                if content in path_dict:
                    path_dict[content].append(abs_path)
                else:
                    path_dict[content] = [abs_path]
                index += 1
        for key, path in path_dict.items():
            if len(path) == 1:
                continue
            else:
                result.append(path)

        return result

