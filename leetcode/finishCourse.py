from collections import defaultdict, deque
# BFS solution (indegree method)
def canFinish(numCourses,prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for src,dest in prerequisites:
        graph[dest].append(src)
        indegree[src] += 1

    queue = deque()
    top_order = []
    cnt = 0 

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.appendleft(i)

    while queue:
        node = queue.pop()
        for ngh in graph[node]:
            indegree[ngh] -= 1
            if indegree[ngh] == 0:
                queue.appendleft(ngh)
        top_order.append(node)
        cnt += 1
    return True if cnt == numCourses else False


# DFS solution (coloring method)
def canFinish2(numCourses,prerequisites):
    WHITE = 1
    GRAY = 2
    BLACK = 3

    graph = defaultdict(list)

    for src,dst in prerequisites:
        graph[src].append(dst)

    color = {k:WHITE for k in range(numCourses)}
    top_order = []

    def dfs(node):
        color[node] = GRAY

        for neighbour in graph[node]:
            if color[neighbour] == WHITE:
                dfs(neighbour)
            elif color[neighbour] == GRAY:
                return False
        color[node] = BLACK
        top_order.append(node)

    for vertex in range(numCourses):
        if color[vertex] == WHITE:
            dfs(vertex)

    return True if len(top_order) == numCourses else False