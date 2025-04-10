class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = [1] * numCourses

        for _ከዛ, _መጀመራያ in  prerequisites:
            graph[_መጀመራያ].append(_ከዛ)


        def cycle(vertex):

            if color[vertex] == 2:
                return True
            if color[vertex] == 3:
                return False

            color[vertex] = 2

            for n in graph[vertex]:
                if color[n] == 2:
                    return True
                
                if cycle(n):
                    return True

            color[vertex] = 3
            return False
        
        


        for i in range(numCourses):
            if cycle(i):
                return False
        return True
        

        

        

