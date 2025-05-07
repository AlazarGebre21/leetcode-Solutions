class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Track how many meetings each room has hosted
        ans = [0] * n

        # Min-heap of available rooms (by room number)
        free_room = list(range(n))
        free_room.sort()  # Make sure heap is valid initially
        # Min-heap of held rooms (by end time)
        held_room = []

        # Sort meetings by start time
        meetings.sort()

        for st, et in meetings:
            # Free rooms whose meetings have ended by the current meeting's start time
            while held_room and held_room[0][0] <= st:
                end_time, room = heappop(held_room)
                heappush(free_room, room)

            if free_room:
                # Assign meeting to the smallest-numbered free room
                room = heappop(free_room)
                heappush(held_room, (et, room))
                ans[room] += 1
            else:
                # No room is free — delay the meeting to the earliest room's free time
                end_time, room = heappop(held_room)
                duration = et - st
                new_end = end_time + duration
                heappush(held_room, (new_end, room))
                ans[room] += 1

        # Return the index of the room with the most meetings
        most_booked = 0
        max_count = 0

        for i in range(n):
            if ans[i] > max_count:
                max_count = ans[i]
                most_booked = i

        return most_booked