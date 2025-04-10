class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        my_dict = {}
        

        def dfs(vertex):

            if vertex not in my_dict:
                my_dict[vertex] = 'red'

            for n in graph[vertex]:
                if n in my_dict:
                    if my_dict[vertex] == my_dict[n]:
                        return False
                else:
                    my_dict[n] = 'blue' if my_dict[vertex] == 'red' else 'red'
                    
                    if not dfs(n):
                        return False

            return True

        for i in range(len(graph)):
            if i not in my_dict:
                if not dfs(i):
                    return False
       
        return True 