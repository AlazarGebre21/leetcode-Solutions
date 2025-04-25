class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       graph = defaultdict(list)
       n = numCourses
       for a, b in prerequisites:
        graph[b].append(a)
       
       color = [0] * n

       def has_cycle(parent):

            color[parent] = 1

            for child in graph[parent]:

                if color[child] == 1:
                    return True
                if color[child] == 0 and has_cycle(child):
                    return True

            color[parent] = 2
            return False

       for i in range(n):
        if color[i] == 0:
            if has_cycle(i):
                return False
        
       return True


            
        




        

        

