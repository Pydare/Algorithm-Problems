import heapq
def min_meetingrooms(intervals):
    if not intervals:
        return 0

    #heap initialization
    free_rooms = []

    #sort the meetings in increasing order of their start time
    intervlas.sort(key=lambda x: x[0])

    #add the first meeting 
    heapq.heappush(free_rooms,intervals[0][1])

    #for all the remaining meeting rooms
    for i in intervals[1:]:

        #if the room due to free up the earliest is free, assign that room to this meeting
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        #if new room is to be assigned, then also we add to the heap,
        #if an old room is allocated, then we have to add to the heap with updated end time
        heapq.heappush(free_rooms,i[1])

    #return the size of the heap
    return len(free_rooms)