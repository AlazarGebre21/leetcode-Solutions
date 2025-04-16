class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        keys = set([0])

    
        

        while queue:
            key = queue.popleft()

            for room in rooms[key]:


                if room not in keys:
                    queue.append(room)
        
                keys.add(room)

        
        return len(keys) == len(rooms)

                
            
