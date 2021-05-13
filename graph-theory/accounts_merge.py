from collections import defaultdict
def accountsMerge(accounts):
    
    """
    ["John", "johnsmith@mail.com", "john00@mail.com"], 
    ["John", "johnnybravo@mail.com"], 
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
    ["Mary", "mary@mail.com"]
    """
    
    em_to_name = {}
    graph = defaultdict(set)
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            em_to_name[email] = name 
            
    seen = set()
    ans = []
    for email in graph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            ans.append([em_to_name[email]] + sorted(component))
            
    return ans