from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.indegrees = 0
        self.out_nodes = []

def can_finish(num_courses,prerequisites):

    graph = defaultdict(Graph)

    total_deps = 0
    for x,y in prerequisites:
        nxt_course, prev_course = x, y
        graph[prev_course].out_nodes.append(nxt_course)
        graph[nxt_course].indegrees += 1
        total_deps += 1
    #start from courses with 0 prerequisites
    q = deque()
    for idx, node in graph.items():
        if node.indegrees == 0:
            q.append(idx)

    removed_edges = 0
    order = []
    while q:
        #pop out course without dependency
        course = q.popleft()
        order.append(course)
        #remove the outgoing edges of courses it points to one by one
        for nxt_course in graph[course].out_nodes:
            graph[nxt_course].indegrees -= 1
            removed_edges += 1
            #we might discover courses w prerequisites removed
            if graph[nxt_course].indegrees == 0:
                q.append(nxt_course)
    print(order)
    if removed_edges == total_deps:
        return True
    else:
        return False

ans = can_finish(4,[[0,1],[1,2],[2,3]])
print(ans)

