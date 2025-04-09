class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        my_dict = {}
        

        def dfs(vertex):

            for i in range(len(graph[vertex])):
                if vertex not in my_dict:
                    my_dict[vertex] = 'red'
                if graph[vertex][i] in my_dict:
                    if my_dict[vertex] == my_dict[graph[vertex][i]]:
                        return False
                    
                else:
                    if my_dict[vertex] == 'red':
                        my_dict[graph[vertex][i]] = 'blue'
                        dfs(graph[vertex][i])
                    else:
                        my_dict[graph[vertex][i]] = 'red'
                        dfs(graph[vertex][i])
            return True

        result = [dfs(i) for i in range(len(graph))]
        print(result)
        return False if False in result else True
                    

                
        
        


            
