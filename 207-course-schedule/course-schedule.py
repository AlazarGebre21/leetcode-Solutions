class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        c = [1] * numCourses

        for _ከዛ, _መጀመራያ in  prerequisites:
            graph[_መጀመራያ].append(_ከዛ)


        def cycle(vertex):

            if c[vertex] == 2:
                return True
            if c[vertex] == 3:
                return False

            c[vertex] = 2

            for n in graph[vertex]:
                if c[n] == 2:
                    return True
                
                if cycle(n):
                    return True

            c[vertex] = 3
            return False
        
        


        for i in range(numCourses):
            if cycle(i):
                return False
        return True
        

        

        

