class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        reachable = [[False] * numCourses for i in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            reachable[pre][course] = True


        que = deque([i for i in range(numCourses) if indegree[i] == 0])        

        while que:
            preq_course = que.popleft()

            for next_course in graph[preq_course]:

                for other_course in range(numCourses):
                    
                    if reachable[other_course][preq_course]:

                        reachable[other_course][next_course] = True
                
                reachable[preq_course][next_course] = True

                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    que.append(next_course)
        

        return [reachable[u][v] for u, v in queries]

