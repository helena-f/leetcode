class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        """

        start = []
        end = []
        for start_val, end_val in intervals:
            start.append(start_val)
            end.append(end_val)
        
        start.sort()
        end.sort()

        max_count = 0
        curr_count = 0
        end_index = 0
        for start_time in start:
            while end_index < len(end) and start_time >= end[end_index]:
                curr_count -= 1
                end_index += 1

            # This meeting starts → need a new room
            curr_count += 1
            max_count = max(max_count, curr_count)

        return max_count