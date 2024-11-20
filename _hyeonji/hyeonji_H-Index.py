def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    # enumerate : (인덱스,값) 반환
    for idx,val in enumerate(citations):
        if idx+1<=val:
            answer=idx+1
            
            
    return answer