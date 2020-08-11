from collections import defaultdict
def find_itinerary(tickets):
    flight_map = defaultdict(list)

    for ticket in tickets:
        origin, dest = ticket[0], ticket[1]
        flight_map[origin].append(dest)

    visit_bitmap = {}

    #sorting the itinerary based on lexical order
    for origin, itinerary in flight_map.items():
        itinerary.sort()
        visit_bitmap[origin] = [False]*len(itinerary)

    flights = len(tickets)
    result = []
    route = ['JFK']
    backtracking('JFK',route)

    return result 

    def backtracking(origin,route):
        if len(route) == flights + 1:
            result = route
            return True

        for i, next_dest in enumerate(flight_map[origin]):
            if not visit_bitmap[origin][i]:
                #mark the visit before next recursion
                visit_bitmap[origin][i] = True
                ret = backtracking(next_dest, route + [next_dest])
                visit_bitmap[origin][i] = False
                if ret:
                    return True

        return False
