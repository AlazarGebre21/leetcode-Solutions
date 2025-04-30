class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chair = []
        for x in range(len(times)):
            heappush(chair, x) 

        order = []

        for i, val in enumerate(times):
            start, leave = val
            order.append((start, True, i))
            order.append((leave, False, i))
        
        order.sort()

        my_dict = {}

        for time, enter, person in order:

            if person in my_dict:
               leaved_chair = my_dict[person]
               my_dict.pop(person)
               heappush(chair, leaved_chair)
            else:
                my_dict[person] = heappop(chair)

                if person == targetFriend:
                    
                    return my_dict[person]
        

