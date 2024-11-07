def solution(numbers, target):
    answer = 0
    
    queue=[0]
    for i in numbers:
        s=[]
        for j in range(len(queue)):
            val=queue.pop()
            s.append(val+i)
            s.append(val-i)
        queue=s.copy()
        
    answer=queue.count(target)
    
    return answer