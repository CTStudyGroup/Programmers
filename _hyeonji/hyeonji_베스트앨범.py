def solution(genres, plays):
    answer = []
    
    # 1번조건. 속한 노래가 많이 재생된 장르
    info_many_plays={}
    for i in range(len(genres)):
        if genres[i] not in info_many_plays:
            info_many_plays[genres[i]]=plays[i]
        else:
            info_many_plays[genres[i]]+=plays[i]

    # 정렬
    sort_info_many_plays=sorted(info_many_plays, key=info_many_plays.get, reverse=True)
    
    # 정보입력 {장르:[(재생횟수,고유번호)]}        
    info_plays={}
    for i in range(len(genres)):
        if genres[i] not in info_plays:
            info_plays[genres[i]]=[(plays[i],i)]
        else:
            info_plays[genres[i]].append((plays[i],i))
    
    # 1번조건. 속한 노래가 많이 재생된 장르를 먼저 수록
    # 2번조건. 장르 내에서 많이 재생된 노래를 먼저 수록
    # 3번조건. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
    for i in sort_info_many_plays:
        # 정렬
        sort_info_plays=sorted(info_plays[i], key=lambda x:(-x[0],x[1]))
        print(sort_info_plays)
        print(len(sort_info_plays))
        if len(sort_info_plays)==1:
            answer.append(sort_info_plays[0][1])
        else:
            for j in range(2):
                answer.append(sort_info_plays[j][1])
                
    return answer