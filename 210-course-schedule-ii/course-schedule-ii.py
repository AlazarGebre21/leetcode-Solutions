class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        graph = defaultdict(list)
        order = []

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        que = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while que:

            course = que.popleft()
            order.append(course)

            for neighbour in graph[course]:


                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    que.append(neighbour)
                

        return order if len(order) == numCourses else []
            


            
            


        



