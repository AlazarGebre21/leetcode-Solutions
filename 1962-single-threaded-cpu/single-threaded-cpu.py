class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
        heap = []
        time = tasks[0][0]
        ans = []

        print(tasks)

        i = 0
        while i < len(tasks):
            enq, proc, indx = tasks[i]
            if enq <= time:
                heappush(heap, (proc,indx))
            else:
                break
            
            i += 1

        while heap:
            # print(f'time{time}')
            # print(heap)

            t, indx = heappop(heap)


            time += t
            ans.append(indx)

            if i < len(tasks) and not heap:
                enq, proc, indx = tasks[i]
                if time < enq:
                    time = enq

           
            while i < len(tasks):
                # print(time)
                enq, proc, indx = tasks[i]
                if enq <= time:
                    heappush(heap, (proc,indx))
                else:
                    break
                
                i += 1
        return ans    

            
