# link : https://leetcode.com/problems/meeting-rooms-ii/solution/

# priority queues

intervals = [[0,30], [5,10], [15,20]]
# print(intervals[0])
# print(intervals[1])

# rooms = 0

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = [] #heap
        intervals.sort(key = lambda x:x[0])
        
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            
            if free_rooms[0]<= i[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)

# for meeting in intervals:
	# print(meeting)
