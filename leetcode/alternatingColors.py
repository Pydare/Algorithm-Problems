import collections
n=
red_edges = [[0,1],[1,2],[2,3],[3,4]]
blue_edges = [[1,2]]

g_blue = collections.defaultdict(set)
g_red = collections.defaultdict(set)
for edge in red_edges:
    u, v = edge
    g_red[u].add(v)
for edge in blue_edges:
    u, v = edge
    g_blue[u].add(v)

res = dict(zip(range(n),[-1]*n))

print(res)