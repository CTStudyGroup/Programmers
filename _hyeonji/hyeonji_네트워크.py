def solution(n, computers):
    answer = 0
    
    visited=[False]*n

    def dfs(v):
        visited[v]=1
        for i in range(n):
            if computers[v][i] and not visited[i]:
                dfs(i)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
            
    return answer