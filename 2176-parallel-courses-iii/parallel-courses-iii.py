class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        months = 0
        graph = defaultdict(list)
        indegree = {x:0 for x in range(1, n + 1)}



        for _from, _to in relations:
            graph[_from].append(_to)
            indegree[_to] += 1
        
        

        heap = [ [time[key-1], key] for key, value in indegree.items() if value == 0]

        heapify(heap)

        # print(heap)

        while heap:
            

            t, course = heappop(heap)


            for i in range(len(heap)):
                heap[i][0] -= t
            
            months += t

            # print(f'course and time {course, t}')
            # print(f'months {months}')
            

            for next_course in graph[course]:
                
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    heappush(heap, [ time[next_course - 1], next_course])
        
        

        
        return months
                    




        