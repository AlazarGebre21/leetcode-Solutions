class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        stack = []
        color = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        


        def dfs(course):

            color[course] = 1

            for after_course in graph[course]:

                if color[after_course] == 1:
                    return True
                
                if color[after_course] == 0 and dfs(after_course):
                    return True
            
            color[course] = 2
            stack.append(course)
            return False
        

        for i in range(numCourses):
            if color[i] == 0:
                if dfs(i):
                    return []

        return stack[::-1]
            


            
            


        



