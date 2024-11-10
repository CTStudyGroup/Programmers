def solution(clothes):
    answer = 0
    
    # 정보 입력.
    info={}
    for i in clothes:
        if i[1] not in info:
            info[i[1]]=1
        else:
            info[i[1]]+=1
    
    case=[]
    for i in info.items():
        case.append(i[1]+1)
    
    comb=1
    for i in case:
        comb*=i
    
    answer=comb-1
        
    return answer