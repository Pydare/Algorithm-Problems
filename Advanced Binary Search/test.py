def efficientJanitor(weight):
    # Write your code here
    res, max_ = float('-inf'), 3.0
    visited = [False]*len(weight)
    
    def dfs(weight,visited,w,tmp,max_):
        nonlocal res
        
        if tmp > res:
            return
        if all(visited):
            res = min(res, tmp)
            return
        for i in range(0,len(weight)):
            if not visited[i]:
                visited[i] = True
                if w + weight[i] <= max_:
                    dfs(weight, visited, w + weight[i], tmp, max_)
                else:
                    dfs(weight, visited, weight[i], tmp+1, max_)
                visited[i] = False

    dfs(weight, visited, 0.0, 1, max_)
    return res

ans = efficientJanitor([1.01,1.99,2.5,1.5,1.01])
print(ans)