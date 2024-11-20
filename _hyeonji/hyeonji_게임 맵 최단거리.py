from collections import deque

def solution(maps):
    answer = 0
    
    dx=[0,1,0,-1] # 동-남-서-북
    dy=[1,0,-1,0]
    
    queue=deque([(0,0)])
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                queue.append([nx,ny])
        
        answer=maps[len(maps)-1][len(maps[0])-1]
    
    # 상대 팀 진영에 도착할 수 없을 때는 -1
    if answer==1:
        answer=-1
    else:
        answer=answer
         
    return answer